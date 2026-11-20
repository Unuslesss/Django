from django import forms
from .models import *


class DepartmentForm(forms.ModelForm):
    class Meta:
        model = Department
        fields = ['name', 'faculty']


class StudentGroupForm(forms.ModelForm):
    class Meta:
        model = StudentGroup
        fields = ['name', 'study_year', 'number', 'course', 'faculty']


class DisciplineForm(forms.ModelForm):
    class Meta:
        model = Discipline
        fields = ['discipline_name']


class TeacherForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = ['full_name', 'birth_year', 'number_of_children', 'id_pol', 'department', 'id_salary', 'id_category', 'photo']


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['lastname', 'firstname', 'middlename', 'birth_year', 'age', 'id_pol', 'group', 'id_scholarship', 'photo']
