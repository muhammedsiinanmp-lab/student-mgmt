from django.shortcuts import render, redirect
from .forms import EnrollmentForm
from .models import Enrollment
# Create your views here.


def enrollments(request):
    if request.method == "POST":
        form = EnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect("enrollments")
    else:
        form = EnrollmentForm()

    enrollments = Enrollment.objects.select_related("student", "course")
    return render(
        request, "enrollment.html", {"form": form, "enrollments": enrollments}
    )
