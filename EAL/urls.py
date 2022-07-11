"""EAL URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import AdminView
from . import EmployeeView
from . import StateCityView
from . import Attend

urlpatterns = [
    path('admin/', admin.site.urls),
    path('adminlogin/',AdminView.AdminLogin),
    path('checkadminlogin',AdminView.CheckAdminLogin),
    path('adminlogout/',AdminView.AdminLogut),

    path('employeelogin/',EmployeeView.EmployeeLogin),
    path('checkemployeelogin/',EmployeeView.CheckEmployeeLogin),
    path('employeedashboard/',EmployeeView.EmployeeDashboard),
    path('employeeinterface/',EmployeeView.EmployeeInterface),
    path('employeesubmit',EmployeeView.EmployeeSubmit),
    path('employeelogout/',EmployeeView.EmployeeLogout),
    path('displayall/',EmployeeView.DisplayAll),
    path('dashboard/',AdminView.Dashboard),
    path('employeeinfo/',EmployeeView.EmployeeInfo),

    path('attend/',Attend.Attend),
    path('attendsubmit',Attend.AttendSubmit),
    path('leave/',Attend.Leave),
    path('leavesubmit',Attend.LeaveSubmit),
    path('employeeattendance/',Attend.ShowAttendance),

    path('fetchallstates/', StateCityView.FetchAllStates),
    path('fetchallcities/', StateCityView.FetchAllCities)
]
