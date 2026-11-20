from django.contrib import admin
from .models import *

admin.site.register(Faculty)
admin.site.register(Department)
admin.site.register(StudentGroup)
admin.site.register(Discipline)
admin.site.register(Teacher)
admin.site.register(Student)
admin.site.register(DiplomaWork)
# Добавь сюда 8-ю модель из конца твоего models.py:
# admin.site.register(НазваниеВосьмойМодели)
