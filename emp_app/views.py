from django.shortcuts import render, HttpResponse
from .models import Employee, Department, Role
from datetime import datetime
from django.db.models import Q
from django.template import loader

# Create your views here.
def index(request):
    return render(request,'index.html')

def all_emp(request):
    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'all_emp.html',context)

def add_emp(request):
    if request.method=="POST":
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=int(request.POST['dept'])
        salary=int(request.POST['salary'])
        bonus=int(request.POST['bonus'])
        role=int(request.POST['role'])
        phone=(request.POST['phone'])

        new_emp = Employee(first_name=first_name,last_name=last_name
                 ,dept_id=dept,salary=salary,bonus=bonus,
                 role_id=role,phone=phone,hire_date=datetime.now())
        new_emp.save()
        return render(request,'add_emp.html',{'msg': "Employee added successfully"})
    elif request.method=='GET':
         
         return render(request,'add_emp.html')
    else:
        return HttpResponse("An Exception occured! Employee not added")


def remove_emp(request,emp_id=0):
    if emp_id:
        try:
            emp_to_be_removed=Employee.objects.get(id=emp_id)
            emp_to_be_removed.delete()
            return render(request,'remove_emp.html',{'msg': "Employee removed successfully"})
            # return HttpResponse('Employee removed successfully')
        except:
            return HttpResponse('Please enter a valid Employee ID')
    #       return render(request,'remove_emp.html',{'msg': "Employee removed successfully"})
    #   except:
    #        return render(request,{'msg':'Please enter a valid Employee ID'})

    emps=Employee.objects.all()
    context={
        'emps':emps
    }
    return render(request,'remove_emp.html',context)

def filter_emp(request):
    if request.method=='POST':
        name=request.POST['name']
        dept=request.POST['name']
        role=request.POST['role']
        emps=Employee.objects.all()
        if name:
            emps=emps.filter(Q(first_name__icontains=name)| Q(last_name__icontains=name))
        if dept:
            emps=emps.filter(dept__name__icontains=dept)
        if role:
            emps=emps.filter(role__name__icontains=role)

        context={
            'emps':emps
        }
        return render(request,'all_emp.html',context)
    elif request.method=='GET':
        return render(request,'filter_emp.html')
    else:
        return HttpResponse("An Exception occured! Employee not added")

 
def dept_name(request):
    depts=Department.objects.all()
    context={
        'depts':depts
    }
    return render(request,'remove_emp.html', context)