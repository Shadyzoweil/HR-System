from django.urls import path
from . import views
from .views import EmployeeListView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
]