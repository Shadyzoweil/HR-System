from django.urls import path
from . import views
from .views import EmployeeListView , LoginView

urlpatterns = [
    path('employees/', EmployeeListView.as_view(), name='employee-list'),
    path("login/", LoginView.as_view(), name="login"),
]