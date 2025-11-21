from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('<int:cources_id>/',views.courses_name, name='courses_name')
]