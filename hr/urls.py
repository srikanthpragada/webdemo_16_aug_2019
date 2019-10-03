from django.urls import path
from . import views, job_views, emp_views

urlpatterns = [
    path('ajaxdemo/', emp_views.ajax_demo),
    path('info/', views.info),
    path('countries/', views.countries_list),
    path('jobs/', job_views.list_jobs),
    path('addjob/', job_views.add_job),
    path('interest/', views.interest),
    path('emp/home/', emp_views.home),
    path('emp/add/', emp_views.add),
    path('emp/list/', emp_views.list_emp),
    path('emp/delete/<int:id>', emp_views.delete),
    path('emp/edit/<int:id>', emp_views.edit),
    path('emp/maxsal', emp_views.maxsal),
    path('emp/search', emp_views.search),
]
