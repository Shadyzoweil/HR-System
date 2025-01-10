# Generated by Django 5.1.4 on 2025-01-10 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('group', models.CharField(choices=[('Normal', 'Normal Employee'), ('HR', 'HR Employee')], default='Normal', max_length=10)),
            ],
        ),
    ]
