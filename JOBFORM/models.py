from django.db import models

# Create your models here.

GENDER_CHOICES = [
    ('', 'SELECT GENDER'),
    ('Male', 'Male'),
    ('Female', 'Female'),
    ('Other', 'Other'),
]

STATE_CHOICES =[
    ('', 'CHOOSE STATES'),
    ('DL', 'Delhi'),
    ('MH', 'Maharashtra'),
    ('KA', 'Karnataka'),
    ('TN', 'Tamil Nadu'),
    ('UP', 'Uttar Pardesh'),
]

JOB_TYPE_CHOICES =[
    ('Full-Time', 'Full-Time'),
    ('Part-Time', 'Part-Time'), 
    ('Remote', 'Remote'),
]



class JobPost(models.Model): 
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    job_type = models.CharField(max_length=50, choices=JOB_TYPE_CHOICES)   
    salary = models.CharField(max_length=20, blank=True)
    description = models.TextField()
    requirements = models.TextField()
    posted_on = models.DateTimeField(auto_now_add=True)

class JobApplication(models.Model):
    job = models.ForeignKey(JobPost, on_delete=models.CASCADE,null = True, blank = True)
    # PERSONAL INFO
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=10)
    dob = models.DateField()
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    profile_photo = models.ImageField(upload_to='APPLICANT_PHOTOS/')

    # ADDRESS
    address = models.CharField(max_length=250)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=2, choices=STATE_CHOICES)
    pincode = models.CharField(max_length=6)

    # EDUCATION
    higest_qualification = models.CharField(max_length=100)
    university_name = models.CharField(max_length=150)
    passing_year = models.IntegerField()

    # EXPERIENCE
    experience = models.FloatField()
    last_company = models.CharField(max_length=150, blank=True, null=True)
    skills = models.CharField(max_length=300)
    resume = models.FileField(upload_to='APPLICANT_RESUMES/')

    # SYSTEM FIELDS
    applied_on = models.DateTimeField(auto_now_add=True)
        