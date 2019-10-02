from django.shortcuts import render, redirect
from .models import Employee
from django.db.models import Avg, Sum, Count
from django.core.exceptions import ObjectDoesNotExist


def home(request):
    summary = Employee.objects.all().aggregate(count=Count("id"),
                                               avgsalary=Avg('salary'),
                                               totalsalary=Sum('salary'))
    return render(request, 'emp_home.html', {'summary': summary})


def add(request):
    return render(request, 'emp_add.html')


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


def list(request):
    return render(request, 'emp_list.html',
                  {'employees': Employee.objects.all()})
