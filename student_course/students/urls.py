from django.urls import path
from . import views

urlpatterns = [
    path('',views.students,name='students'),
    path('delete/<int:id>/',views.delete_student,name='delete_student'),
]