from django.urls import path
from . import views, job_views

urlpatterns = [
    path('info/', views.info),
    path('countries/', views.countries_list),
    path('jobs/', job_views.list_jobs),
    path('addjob/', job_views.add_job),
]
