from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSerializer
# def employees(request):
#     return HttpResponse("Hello world!")


class EmployeeListView(APIView):
    def get(self, request):
        employees = Employee.objects.all()  # Get all employees
        serializer = EmployeeSerializer(employees, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class LoginView(APIView):
    def post(self, request):
        email = request.data.get("email")
        password = request.data.get("password")
        try:
            employee = Employee.objects.get(email=email)

            if employee.group == "HR" and employee.password == password: 
                # Return user details if HR
                serializer = EmployeeSerializer(employee)
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response({"message": "Access denied. Only HR employees can log in."}, status=status.HTTP_403_FORBIDDEN)
        except Employee.DoesNotExist:
            return Response({"message": "Employee not found."}, status=status.HTTP_404_NOT_FOUND)