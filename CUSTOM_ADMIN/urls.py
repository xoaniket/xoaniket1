from django.urls import path
from . import views
app_name = "custom_admin" 

urlpatterns = [
     path('', views.dashboard1, name='dashboard1'),


    

     # Jobs CRUD
     path('jobs/', views.joblist, name = 'jobs_list'),
     path('jobs/add/', views.job_add, name = 'job_add'),
     path('jobs/edit/<int:job_id>/', views.job_edit, name = 'job_edit'),
     path('jobs/del/<int:job_id>/', views.job_del, name = 'job_del'),


     # Applications
     path('application/', views.all_applications, name = 'app_list'),
     path('del/<int:pk>/', views.delete, name = 'del_app'),

     # Users
     path('users/', views.userlist, name = 'user_list'),
   

]