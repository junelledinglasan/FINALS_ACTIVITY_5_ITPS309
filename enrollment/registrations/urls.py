from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_list, name='registration_list'),
    path('<int:registration_id>/',views.registration_details, name='registration_details')
]