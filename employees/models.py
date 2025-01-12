from django.db import models

class Employee(models.Model):
    EMPLOYEE_GROUPS = [
        ('Normal', 'Normal Employee'),
        ('HR', 'HR Employee'),
    ]

    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    group = models.CharField(max_length=10, choices=EMPLOYEE_GROUPS, default='Normal')
    password = models.CharField(max_length=128)  # Store plain text passwords

    def __str__(self):
        return f"{self.name} ({self.group}) - {self.email}"
