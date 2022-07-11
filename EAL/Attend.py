from django.shortcuts import render
from . import Pool
from . import PoolDict

def Attend(request):
    try:
        result=request.session['EMPLOYEE']
        print(result)
        return render(request,"Attend.html",{'result':result})
    except Exception as e:
        print(e)
        return render(request,"Attend.html")

def AttendSubmit(request):
    try:
        employeeid=request.POST['employeeid']
        employeename=request.POST['name']
        currentdate=request.POST['currentdate']
        attendtime=request.POST['attendtime']
        q="insert into attend(employeeid,employeename,date,attendtime)values({},'{}','{}','{}')".format(employeeid,employeename,currentdate,attendtime)
        print(q)
        db,cmd=PoolDict.ConnectionPool()
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, 'Attend.html',{'msg':'Saved'})

    except Exception as e:
        print("Error:",e)
        return render(request, 'Attend.html',{'msg':'Not Saved'})

def Leave(request):
    try:
        result=request.session['EMPLOYEE']
        print(result)
        return render(request,"Leave.html",{'result':result})
    except Exception as e:
        print(e)
        return render(request,"Leave.html")

def LeaveSubmit(request):
    try:
        date=request.POST['currentdate']
        leavetime=request.POST['leavetime']
        q="update attend set leavetime='{}' where date='{}'".format(leavetime,date)
        print(q)
        db,cmd=Pool.ConnectionPool()
        cmd.execute(q)
        db.commit()
        db.close()
        return render(request, 'Leave.html',{'msg':'Saved'})

    except Exception as e:
        print("Error:",e)
        return render(request, 'Leave.html',{'msg':'Not Saved'})

def ShowAttendance(request):
    try:
        db,cmd=Pool.ConnectionPool()
        q="select * from attend"
        cmd.execute(q)
        rows=cmd.fetchall()
        db.close()
        return render(request,'EmployeeAttendance.html',{'rows':rows})

    except Exception as e:
        print(e)
        return  render(request,'EmployeeAttendance.html',{'rows': []})
