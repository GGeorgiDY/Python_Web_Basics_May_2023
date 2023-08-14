from django.urls import path

from models2.web.views import index, delete_employee, department_details

urlpatterns = (
    path('', index, name='index'),
    path('delete/<int:pk>/', delete_employee, name='delete employee'),
    path('department/<int:pk>/', department_details, name='details department'),
)