from django.db import models

# Create your models here.
class Student(models.Model):
    roll_no = models.TextField()
    name = models.TextField(max_length = 40)
    stud_class = models.TextField()
    department = models.TextField()
""" bu clasni yaratib bo'lgach uni migratsiya qilib olamiz
python manage.py makemigrations
python manage.py migrate
"""
