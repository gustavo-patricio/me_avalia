from django.contrib import admin
from django.contrib.auth.models import User
from app import models

admin.site.site_header = 'Me Avalia'

admin.site.register(models.Student)
admin.site.register(models.Rating)
admin.site.register(models.Teacher)
admin.site.register(models.Course)
admin.site.register(models.Classroom)
admin.site.register(models.ClassroomStudent)
admin.site.register(models.UniversityClass)


