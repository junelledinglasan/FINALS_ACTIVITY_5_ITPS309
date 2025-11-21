from django import forms
from .models import Grades , Course
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['course_id', 'course_subject', 'units', 'description', 'department']

class GradesForm(forms.ModelForm):
    class Meta:
        model = Grades
        fields = ['Grade_id', 'student_name', 'course_taken', 'grade', 'remark']

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']