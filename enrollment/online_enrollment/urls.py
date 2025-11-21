from django.urls import path
from . import views
from .views import UserLoginView, UserLogoutView

urlpatterns = [
    path('subjects/', views.subjects_list, name="subjects_list"),
    path('courses/', views.courses_list, name="courses_list"),
    path('grades/', views.grades_list, name="grades_list"),
    path('notification/', views.notification_list, name="notification_list"),
    path('attendance/', views.attendance_list, name="attendance_list"),
    path('addcourse/', views.add_course, name="add_course"),
    path('course/edit/<int:pk>', views.edit_course, name="edit_course"),
    path('addgrades/', views.add_grades, name="add_grades"),
    path('grades/edit/<int:pk>', views.edit_grades, name="edit_grades"),
    path('register/', views.register, name='register'),
    path('login/', UserLoginView.as_view(), name='user_login'),
    path('logout/', UserLogoutView.as_view(), name='user_logout'),
    path('profile/', views.student_profile, name='student_profile'),
]