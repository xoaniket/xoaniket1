from django.urls import path
from . import views
from django.views.generic import RedirectView
from .views import CustomLoginView
from django.contrib.auth.decorators import login_required

urlpatterns = [

    # ALL JOB POST
    path('job/', login_required(views.job_list), name='job_list'),
    # JOB DETAIL
    path('job/<int:pk>/', login_required(views.job_detail), name='job_detail'),
    path('about/', login_required(views.about), name='about'),
    path('del/<int:pk>/', views.delete, name='delete'),



    #ADMIN PAGE
    path('applications/', views.all_applications, name= 'all_applocations'),


    

    # AUTH URLS
    path('signup/', views.signup, name='signup'), 
    path('', RedirectView.as_view(url='/accounts/login/', permanent=False)),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', views.customlogout, name= 'logout'),
 ] 