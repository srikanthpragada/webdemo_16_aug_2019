from django.views.generic import TemplateView, ListView
from .models import Employee


class AboutView(TemplateView):
    template_name = "about.html"


class EmployeesListView(ListView):
    model = Employee
    template_name = 'emplist.html'
    context_object_name = "employees"

