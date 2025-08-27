from django.shortcuts import redirect, render
from .form import JobApplicationForm, SignupForm,LoginForm
from .models import JobApplication,JobPost
 
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib import messages  
from django.http import HttpResponse
from django.template.loader import render_to_string
from xhtml2pdf import pisa


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

def delete(request,pk):
    form = JobApplication.objects.get(pk=pk)
    form.delete()
    return redirect('/applications/')

def application_pdf(request,pk):
    application = JobApplication.objects.get(pk=pk)

    if application.profile_photo:
        profile_photo_url = request.build_absolute_uri(application.profile_photo.url)

    if application.resume:
        resume_url = request.build_absolute_uri(application.resume.url)

    html = render_to_string("application_pdf.html", {'application':application, "profile_photo_url": profile_photo_url,
        "resume_url": resume_url,})

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="application_{pk}.pdf"'  

    pisa.CreatePDF(html, dest=response)
    return response  
    

# ALL THE JOBS ..........................................................................

@login_required
def job_list(request):
    jobs =  JobPost.objects.all().order_by('-posted_on')
    return render(request, 'job_list.html', {'jobs':jobs}) 

# DETAIL ABOUT THE SPECIFIC JOB AND FORM................................................

@login_required
def job_detail(request,pk):
     job = JobPost.objects.get(pk = pk)
     if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.instance.job = job
            form.save()
            messages.success(request, "✅ Application submitted for this job!")
            return redirect('/job/')
        else:
               print(form.errors)   # DEBUG
               messages.error(request, f"❌ Failed to apply for this job. Errors: {form.errors}")
     else:
        form = JobApplicationForm()

     return render(request, 'job_detail.html', {'form':form,'job':job})

@login_required
def about(request):
    return render(request,'about.html')

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



def customlogout(request):
    logout(request)
    return redirect('login')

class CustomLoginView(LoginView):
    authentication_form = LoginForm 
    template_name = 'registration/login.html'





