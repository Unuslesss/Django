from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import *
from .forms import *


def home_view(request):
    return render(request, 'lect1/home.html')


def contacts_view(request):
    return render(request, 'lect1/contacts.html')


def location_view(request):
    return render(request, 'lect1/location.html')


class DepartmentListView(ListView):
    model = Department
    template_name = 'lect1/departments/department_list.html'
    context_object_name = 'departments'


class DepartmentDetailView(DetailView):
    model = Department
    template_name = 'lect1/departments/department_detail.html'
    context_object_name = 'department'


class DepartmentCreateView(CreateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'lect1/departments/department_form.html'
    success_url = reverse_lazy('university:department_list')


class DepartmentUpdateView(UpdateView):
    model = Department
    form_class = DepartmentForm
    template_name = 'lect1/departments/department_form.html'
    success_url = reverse_lazy('university:department_list')


class DepartmentDeleteView(DeleteView):
    model = Department
    template_name = 'lect1/departments/department_confirm_delete.html'
    success_url = reverse_lazy('university:department_list')


class GroupListView(ListView):
    model = StudentGroup
    template_name = 'lect1/groups/group_list.html'
    context_object_name = 'groups'


class GroupDetailView(DetailView):
    model = StudentGroup
    template_name = 'lect1/groups/group_detail.html'
    context_object_name = 'group'


class GroupCreateView(CreateView):
    model = StudentGroup
    form_class = StudentGroupForm
    template_name = 'lect1/groups/group_form.html'
    success_url = reverse_lazy('university:group_list')


class GroupUpdateView(UpdateView):
    model = StudentGroup
    form_class = StudentGroupForm
    template_name = 'lect1/groups/group_form.html'
    success_url = reverse_lazy('university:group_list')


class GroupDeleteView(DeleteView):
    model = StudentGroup
    template_name = 'lect1/groups/group_confirm_delete.html'
    success_url = reverse_lazy('university:group_list')


class DisciplineListView(ListView):
    model = Discipline
    template_name = 'lect1/disciplines/discipline_list.html'
    context_object_name = 'disciplines'


class DisciplineDetailView(DetailView):
    model = Discipline
    template_name = 'lect1/disciplines/discipline_detail.html'
    context_object_name = 'discipline'


class DisciplineCreateView(CreateView):
    model = Discipline
    form_class = DisciplineForm
    template_name = 'lect1/disciplines/discipline_form.html'
    success_url = reverse_lazy('university:discipline_list')


class DisciplineUpdateView(UpdateView):
    model = Discipline
    form_class = DisciplineForm
    template_name = 'lect1/disciplines/discipline_form.html'
    success_url = reverse_lazy('university:discipline_list')


class DisciplineDeleteView(DeleteView):
    model = Discipline
    template_name = 'lect1/disciplines/discipline_confirm_delete.html'
    success_url = reverse_lazy('university:discipline_list')


class TeacherListView(ListView):
    model = Teacher
    template_name = 'lect1/teachers/teacher_list.html'
    context_object_name = 'teachers'


class TeacherDetailView(DetailView):
    model = Teacher
    template_name = 'lect1/teachers/teacher_detail.html'
    context_object_name = 'teacher'


class TeacherCreateView(CreateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'lect1/teachers/teacher_form.html'
    success_url = reverse_lazy('university:teacher_list')


class TeacherUpdateView(UpdateView):
    model = Teacher
    form_class = TeacherForm
    template_name = 'lect1/teachers/teacher_form.html'
    success_url = reverse_lazy('university:teacher_list')


class TeacherDeleteView(DeleteView):
    model = Teacher
    template_name = 'lect1/teachers/teacher_confirm_delete.html'
    success_url = reverse_lazy('university:teacher_list')


class StudentListView(ListView):
    model = Student
    template_name = 'lect1/students/student_list.html'
    context_object_name = 'students'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'lect1/students/student_detail.html'
    context_object_name = 'student'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    template_name = 'lect1/students/student_form.html'
    success_url = reverse_lazy('university:student_list')


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    template_name = 'lect1/students/student_form.html'
    success_url = reverse_lazy('university:student_list')


class StudentDeleteView(DeleteView):
    model = Student
    template_name = 'lect1/students/student_confirm_delete.html'
    success_url = reverse_lazy('university:student_list')
