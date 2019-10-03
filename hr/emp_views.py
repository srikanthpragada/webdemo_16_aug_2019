from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm
from django.db.models import Avg, Sum, Count, Max
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse, JsonResponse



def home(request):
    summary = Employee.objects.all().aggregate(count=Count("id"),
                                               avgsalary=Avg('salary'),
                                               totalsalary=Sum('salary'))
    return render(request, 'emp_home.html', {'summary': summary})


def add(request):
    if request.method == "GET":
        f = EmployeeForm()
        return render(request, 'emp_add.html',{"form" : f})
    else:
        f = EmployeeForm(data = request.POST)
        if f.is_valid():
            f.save()   # insert into table
            return redirect("/hr/emp/list")
        else:
            return render(request, 'emp_add.html',{"form" : f})


def delete(request, id):
    try:
        e = Employee.objects.get(id=id)
        e.delete()
        return redirect("/hr/emp/list")
    except ObjectDoesNotExist:
        message = "Sorry! Employee Id Not Found!"
    except:
        message = "Sorry! Could not delete employee!"

    return render(request, 'emp_delete.html', {'message': message})


def list_emp(request):
    return render(request, 'emp_list.html',
                  {'employees': Employee.objects.all()})


def edit(request,id):
    e = Employee.objects.get(id = id)
    if request.method == "GET":
        f = EmployeeForm(instance=e)
        return render(request, 'emp_edit.html',{"form" : f})
    else:
        f = EmployeeForm(instance=e, data = request.POST)
        if f.is_valid():
            f.save()   # update into table
            return redirect("/hr/emp/list")
        else:
            return render(request, 'emp_edit.html',{"form" : f})

def maxsal(request):
    summary = Employee.objects.all().aggregate(maxsal = Max('salary'))
    return HttpResponse( summary['maxsal'])

def ajax_demo(request):
    return render(request, 'ajax_demo.html')


def search(request):
    name = request.GET['name']
    emps = Employee.objects.filter(fullname__contains = name)
    emplist = list(emps.values())  # Convert Employee object to dict
    return JsonResponse(emplist, safe=False)