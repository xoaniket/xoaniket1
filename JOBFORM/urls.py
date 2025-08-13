from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import CustomLoginView

urlpatterns = [

    # ALL JOB POST
    path('job/', views.job_list, name='job_list'),
    # JOB DETAIL
    path('job/<int:pk>/', views.job_detail, name='job_detail'),
    path('about/', views.about, name='about'),



    #ADMIN PAGE
    path('applications/', views.all_applications, name= 'all_applocations'),


    

    # AUTH URLS
    path('signup/', views.signup, name='signup'), 
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.customlogout, name= 'logout'),
 ] 