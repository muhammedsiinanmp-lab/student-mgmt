from django.shortcuts import render, redirect
from .forms import StudentForm
from .models import Student
# Create your views here.


def students(request):
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("students")

    form = StudentForm()
    students = Student.objects.all()

    return render(request, "student.html", {"form": form, "students": students})

def delete_student(request,id):
    if request.method == 'POST':
        student = Student.objects.get(id = id)
        student.delete()
        return redirect('students')
