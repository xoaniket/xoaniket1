from django import forms
from JOBFORM.models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'
