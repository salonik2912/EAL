from django.shortcuts import render
import uuid
import random
from . import Pool
from . import PoolDict

def EmployeeLogin(request):
    try:
        result = request.session['EMPLOYEE']
        return render(request, 'EmployeeDashboard.html', {'result': result})
    except Exception as e:
        return render(request, 'EmployeeLogin.html')

def CheckEmployeeLogin(request):
    try:
        email = request.GET['email']
        password = request.GET['password']
        db, cmd = PoolDict.ConnectionPool()
        q = "select * from employee where email='{}' and password='{}'".format(email, password)
        cmd.execute(q)
        result = cmd.fetchone()
        print(result)
        db.close()
        if(result):
            request.session['EMPLOYEE']=result
            return render(request, 'EmployeeDashboard.html', {'result': result})
        else:
            return render(request, 'EmployeeLogin.html', {'result': result,'msg':'Invalid Email/Password'})
        
        
    except Exception as e:
        print(e)
        return render(request, 'EmployeeLogin.html', {'result': {},'msg':'Server Error '})

def EmployeeLogout(request):
    del request.session['EMPLOYEE']
    return render(request,'EmployeeLogin.html')

def EmployeeInterface(request):
    try:
        #result=request.session['ADMIN']
        return render(request,'EmployeeInterface.html')

    except Exception as e:
        return render(request, 'AdminLogin.html')

def EmployeeSubmit(request):
    try:
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        gender = request.POST['gender']
        birthdate = request.POST['birthdate']
        paddress = request.POST['paddress']
        states = request.POST['states']
        city = request.POST['city']
        caddress = request.POST['caddress']
        emailaddress = request.POST['emailaddress']
        mobilenumber = request.POST['mobilenumber']
        designation = request.POST['designation']

        picture = request.FILES['picture']
        filename = str(uuid.uuid4()) + picture.name[picture.name.rfind('.'):]
        password = "".join(random.sample(['1', 'j', 'd', '@', '#', '9', '$'], k=7))

        q = "insert into employee (firstname, lastname, gender, dob, paddress, stateid, cityid, caddress, email, mobileno, designation, picture, password) values ('{}', '{}', '{}', '{}', '{}', {}, {}, '{}','{}', '{}', '{}', '{}', '{}')".format(firstname, lastname, gender, birthdate, paddress, states, city, caddress, emailaddress, mobilenumber,designation, filename, password)
        print(q)
        db, cmd = Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        F = open("D:/EAL/assets/" + filename, "wb")
        for chunk in picture.chunks():
            F.write(chunk)
        F.close()
        db.close()
        return render(request, 'EmployeeInterface.html',{'msg':'Record Submitted Successfully'})

    except Exception as e:
        print("Error :", e)
        return render(request, "EmployeeInterface.html", {'msg': 'Fail to Submit Record'})

def DisplayAll(request):
    try:
        db, cmd = Pool.ConnectionPool()
        q = "select E.*,(select C.cityname from Cities C where C.cityid = E.cityid), (select S.statename from States S where S.stateid = E.stateid) from employee E"
        cmd.execute(q)
        rows = cmd.fetchall()
        db.close()
        return render(request, "DisplayAllEmployee.html", {'rows': rows})
    except Exception as e:
        print(e)
        return render(request, "DisplayAllEmployee.html", {'rows': []})

def EmployeeInfo(request):
    try:
        result=request.session['EMPLOYEE']
        print(result)
        return render(request, 'EmployeeInfo.html',{'result':result})

    except Exception as e:
        print(e)
        return render(request, 'EmployeeInfo.html',{'result':result})

def EmployeeDashboard(request):
    try:
        return render(request, 'EmployeeDashboard.html')

    except Exception as e:
        print(e)
        return render(request, 'EmployeeDashboard.html')
