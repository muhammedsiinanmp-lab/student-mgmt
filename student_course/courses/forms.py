from django import forms
from .models import Courses

class CourseForm(forms.ModelForm):
    class Meta:
        model = Courses
        fields = ['title','code','duration_weeks']
        