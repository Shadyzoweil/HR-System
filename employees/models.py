from django.db import models

# Create your models here.

class Employee(models.Model):
    EMPLOYEE_GROUPS = [
        ('Normal', 'Normal Employee'),
        ('HR', 'HR Employee'),
    ]

    name = models.CharField(max_length=255)  
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=10, choices=EMPLOYEE_GROUPS, default='Normal')

    def __str__(self):
        return f"{self.name} ({self.group}) - {self.email}"
