from django.shortcuts import redirect, render
from .form import JobApplicationForm, SignupForm,LoginForm
from .models import JobApplication,JobPost
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.
def apply_job(request):

    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('admin/')
    else:
        form = JobApplicationForm()

    return render(request, 'job_apply.html', {'form':form})  


# ALL THE APPLICATIONS.............................................................
def all_applications(request):
    form = JobApplication.objects.all().order_by('-applied_on')    
    return render (request, 'all_application.html', {'form':form})

# ALL THE JOBS ..........................................................................

def job_list(request):
    jobs =  JobPost.objects.all().order_by('-posted_on')
    return render(request, 'job_list.html', {'jobs':jobs}) 

# DETAIL ABOUT THE SPECIFIC JOB AND FORM................................................
def job_detail(request,pk):
     job = JobPost.objects.get(pk = pk)
     if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.job = job
            form.save()
            return redirect('/job/')
     else:
        form = JobApplicationForm()

     return render(request, 'job_detail.html', {'form':form,'job':job})

# SIGNUP PAGE...................................................................
def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()
    return render(request,'registration/signup.html', {'form':form})    

def about(request):
    return render(request,'about.html')

def customlogout(request):
    logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    authentication_form = LoginForm   
    template_name = 'registration/login.html'

