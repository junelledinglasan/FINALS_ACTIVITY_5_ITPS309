from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required 
from .forms import CourseForm, GradesForm, UserRegisterForm 
from .models import Subjects,Course,Grades,Notification,Attendance


class UserLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    next_page = 'add_course'

class UserLogoutView(LogoutView):
    next_page = 'user_login' 

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user_login') 
    else:
        form = UserRegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def student_profile(request):
    return render(request, 'profile.html')

@login_required 
def subjects_list(request):
    subjects = Subjects.objects.all()
    return render (request, 'subjects_list.html', {'subjects': subjects})

@login_required
def courses_list(request):
    courses = Course.objects.all() 
    return render (request, 'courses_list.html', {'courses': courses})

@login_required
def grades_list(request):
    grades = Grades.objects.all()
    return render (request, 'grades_list.html', {'grades': grades})

@login_required
def notification_list(request):
    notification = Notification.objects.all()
    return render (request, 'notification_list.html', {'notification': notification})

@login_required
def attendance_list(request):
    attendance = Attendance.objects.all()
    return render (request, 'attendance_list.html', {'attendance': attendance})


@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses_list') 
    else:
        form = CourseForm()
    
    courses = Course.objects.all()
    return render(request, 'add_course.html', {'form':form, 'courses': courses}) 

# --- COURSE EDIT FUNCTION ---
@login_required
def edit_course(request, pk):
    course = get_object_or_404(Course, pk=pk)
    form = CourseForm(request.POST or None, instance=course)
    if form.is_valid():
        form.save()
        return redirect('courses_list') 
    return render(request, 'edit_course.html', {'form':form})


@login_required
def add_grades(request):
    if request.method == 'POST':
        form = GradesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('grades_list') 
    else:
        form = GradesForm()
    
    grades = Grades.objects.all()
    return render(request, 'add_grade.html', {'form': form, 'grades': grades})

# --- GRADES EDIT FUNCTION ---
@login_required
def edit_grades(request, pk):
    grade = get_object_or_404(Grades, pk=pk)
    form = GradesForm(request.POST or None, instance=grade)
    if form.is_valid():
        form.save()
        return redirect('grades_list')
    return render(request, 'edit_grade.html', {'form':form})
