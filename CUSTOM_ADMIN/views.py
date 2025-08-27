from django.shortcuts import redirect, render
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User  
from JOBFORM.models import JobApplication,JobPost
from .forms import JobPostForm
from django.contrib import messages  

# Create your views here.
# CUSTOM ADMIN.............................

def superuser_required(view_func):
    return user_passes_test(lambda u: u.is_superuser)(view_func)

@superuser_required
def userlist(request):
    users = User.objects.all()
    
    return render(request, "custom_admin/user_list.html", {'users': users})  



# ----- Jobs -----

@superuser_required
def joblist(request):
    jobs = JobPost.objects.all()
    return render(request, 'custom_admin/job_list.html', {'jobs':jobs})


@superuser_required
def job_add(request):
    Add = JobPost.objects.all()
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_list')
    else:
        form = JobPostForm()
    return render(request, 'custom_admin/job_form.html', {'form': form, 'Add': Add})


@superuser_required
def job_edit(request, job_id):
    job = JobPost.objects.get(id=job_id)
    if request.method == 'POST':
        form = JobPostForm(request.POST, request.FILES, instance=job)
        if form.is_valid():
            form.save()
            return redirect('custom_admin:jobs_list')
    else:
        form = JobPostForm(instance=job)
    return render(request, 'custom_admin/job_form.html', {'form': form, 'job':job})


@superuser_required
def job_del(request,job_id):
    job = JobPost.objects.get(id=job_id)
    job.delete()
    return redirect('custom_admin:jobs_list')
    







@superuser_required
def all_applications(request):
    app = JobApplication.objects.all().order_by('-applied_on')    
    return render (request, 'custom_admin/app_list.html', {'app':app})

def delete(request,pk):
    form = JobApplication.objects.get(pk=pk)
    form.delete()
    return redirect('/myadmin/application/')




# Dashboard
@superuser_required
def dashboard1(request):
    jobs_count = JobPost.objects.count()
    apps_count = JobApplication.objects.count()
    users_count = User.objects.count()
    return render(request, 'custom_admin/dashboard.html', {
        'jobs_count': jobs_count,
        'apps_count': apps_count,
        'users_count': users_count
    })   