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