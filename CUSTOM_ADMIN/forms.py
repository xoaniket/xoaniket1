from django import forms
from JOBFORM.models import JobPost

class JobPostForm(forms.ModelForm):
    class Meta:
        model = JobPost
        fields = '__all__'

        widgets = {

            'title':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter Title'}),
            'company':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter The Company Name'}),
            'location':forms.TextInput(attrs={'class':'form-control'}),
            'job_type':forms.TextInput(attrs={'class':'form-control'}),
            'salary':forms.TextInput(attrs={'class':'form-control'}),
            'description':forms.Textarea(attrs={'class':'form-control'}),
            'requirements':forms.Textarea(attrs={'class':'form-control'}),
        }
