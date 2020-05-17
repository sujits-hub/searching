from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from searchapp.models import Employee,Company

def home(request):
    return render(request,"home.html")
def employee(request):
    return render(request,"employee.html")
def company(request):
    return render(request,"company.html")
def searchemp(request):
    return render(request,"searchemp.html")
def searchcom(request):
    return render(request,"searchcom.html")
def companydata(request):
    job_profile_id= request.GET['job_profile_id']
    job_profile= request.GET['job_profile']
    salary= request.GET['salary']
    employee_id= request.GET['employee_id']
    Company(job_profile_id=job_profile_id,job_profile=job_profile,salary=salary,employee_id=employee_id).save()
    msg="record stored successfully"
    return render(request,"company.html",{'msg':msg})
 
def employeedata(request):
     employee_id=request.GET['employee_id']
     name=request.GET['name']
     age=request.GET['age']
     mobile_no=request.GET['mobile_no']
     city=request.GET['city']
     Employee(employee_id=employee_id,name=name,age=age,mobile_no=mobile_no,city=city).save()
     msg="record store successfully"
     return render(request,"employee.html",{'msg':msg})

def searchempdata(request):
    data=request.GET['data']
    info=Employee.objects.filter(name__iexact=data)
    return render(request,"searchemp.html",{'info':info})
def searchcomdata(request):
    data=request.GET['data']
    return render(request,"searchcom.html") 
def viewempdata(request):
     empdata=Employee.objects.all()
     cnt=Employee.objects.count()
     return render(request,"viewempdata.html",{'empdata':empdata,'cnt':cnt})
    
def viewcomdata(request):
     comdata=Company.objects.all()
     cnt=Company.objects.count()
     return render(request,"viewcomdata.html",{'comdata':comdata,'cnt':cnt})


# Create your views here.
