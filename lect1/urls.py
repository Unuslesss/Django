from django.urls import path
from .views import *

app_name = 'university'

urlpatterns = [
    path('', home_view, name='home'),
    path('about/', contacts_view, name='about'),
    path('about/contacts/', contacts_view, name='contacts'),
    path('about/location/', location_view, name='location'),

    # 1. Кафедры
    path('departments/', DepartmentListView.as_view(), name='department_list'),
    path('departments/<int:pk>/', DepartmentDetailView.as_view(), name='department_detail'),
    path('departments/create/', DepartmentCreateView.as_view(), name='department_create'),
    path('departments/<int:pk>/update/', DepartmentUpdateView.as_view(), name='department_update'),
    path('departments/<int:pk>/delete/', DepartmentDeleteView.as_view(), name='department_delete'),

    # 2. Учебные группы
    path('groups/', GroupListView.as_view(), name='group_list'),
    path('groups/<int:pk>/', GroupDetailView.as_view(), name='group_detail'),
    path('groups/create/', GroupCreateView.as_view(), name='group_create'),
    path('groups/<int:pk>/update/', GroupUpdateView.as_view(), name='group_update'),
    path('groups/<int:pk>/delete/', GroupDeleteView.as_view(), name='group_delete'),

    # 3. Дисциплины
    path('disciplines/', DisciplineListView.as_view(), name='discipline_list'),
    path('disciplines/<int:pk>/', DisciplineDetailView.as_view(), name='discipline_detail'),
    path('disciplines/create/', DisciplineCreateView.as_view(), name='discipline_create'),
    path('disciplines/<int:pk>/update/', DisciplineUpdateView.as_view(), name='discipline_update'),
    path('disciplines/<int:pk>/delete/', DisciplineDeleteView.as_view(), name='discipline_delete'),

    # 4. Преподаватели
    path('teachers/', TeacherListView.as_view(), name='teacher_list'),
    path('teachers/<int:pk>/', TeacherDetailView.as_view(), name='teacher_detail'),
    path('teachers/create/', TeacherCreateView.as_view(), name='teacher_create'),
    path('teachers/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher_update'),
    path('teachers/<int:pk>/delete/', TeacherDeleteView.as_view(), name='teacher_delete'),

    # 5. Студенты
    path('students/', StudentListView.as_view(), name='student_list'),
    path('students/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
    path('students/create/', StudentCreateView.as_view(), name='student_create'),
    path('students/<int:pk>/update/', StudentUpdateView.as_view(), name='student_update'),
    path('students/<int:pk>/delete/', StudentDeleteView.as_view(), name='student_delete'),
]
