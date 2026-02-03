from django.shortcuts import render,redirect
from .models import Courses
from .forms import CourseForm

# Create your views here.

def courses(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('courses')
    
    form = CourseForm()
    courses = Courses.objects.all()

    return render(request,'courses.html',{
        'form':form,
        'courses':courses
    })