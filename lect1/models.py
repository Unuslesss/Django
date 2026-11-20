from django.db import models

MAX_LENGTH = 255


class Faculty(models.Model):
    id_faculty = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name='Название факультета')
    dean_fullname = models.CharField(max_length=150, verbose_name='ФИО декана')

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'faculty'
        verbose_name = 'Факультет'
        verbose_name_plural = 'Факультеты'


class Department(models.Model):
    id_department = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название кафедры')
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, db_column='id_faculty', verbose_name='Факультет')

    def __str__(self):
        return str(self.name)

    class Meta:
        db_table = 'department'
        verbose_name = 'Кафедра'
        verbose_name_plural = 'Кафедры'


class StudentGroup(models.Model):
    id_group = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name='Название группы')
    study_year = models.IntegerField(verbose_name='Год набора')
    number = models.IntegerField(verbose_name='Номер группы')
    course = models.IntegerField(verbose_name='Курс')
    faculty = models.ForeignKey(Faculty, on_delete=models.DO_NOTHING, db_column='id_faculty', verbose_name='Факультет')

    def __str__(self):
        return f"{self.name} ({self.course} курс)"

    class Meta:
        db_table = 'student_group'
        verbose_name = 'Учебная группа'
        verbose_name_plural = 'Учебные группы'


class Discipline(models.Model):
    id_discipline = models.AutoField(primary_key=True)
    discipline_name = models.CharField(max_length=50, verbose_name='Наименование дисциплины')

    def __str__(self):
        return str(self.discipline_name)

    class Meta:
        db_table = 'discipline'
        verbose_name = 'Дисциплина'
        verbose_name_plural = 'Дисциплины'


class Teacher(models.Model):
    id_teacher = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, verbose_name='ФИО преподавателя')
    birth_year = models.DateField(verbose_name='Дата рождения (ГГГГ-ММ-ДД)')
    number_of_children = models.IntegerField(default=0, verbose_name='Количество детей')
    id_pol = models.IntegerField(default=1, verbose_name='Код пола (1 или 2)')
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, db_column='id_department', verbose_name='Кафедра')
    id_salary = models.IntegerField(default=1, verbose_name='Код оклада (1-4)')
    id_category = models.IntegerField(default=1, verbose_name='Код категории (1-3)')
    photo = models.ImageField(upload_to='teachers/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return str(self.full_name)

    class Meta:
        db_table = 'teacher'
        verbose_name = 'Преподаватель'
        verbose_name_plural = 'Преподаватели'


class Student(models.Model):
    id_student = models.AutoField(primary_key=True)
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    firstname = models.CharField(max_length=50, verbose_name='Имя')
    middlename = models.CharField(max_length=50, null=True, blank=True, verbose_name='Отчество')
    birth_year = models.IntegerField(verbose_name='Год рождения')
    age = models.IntegerField(verbose_name='Возраст (от 16 лет)')
    id_pol = models.IntegerField(default=1, verbose_name='Код пола (1 или 2)')
    group = models.ForeignKey(StudentGroup, on_delete=models.DO_NOTHING, db_column='id_group', verbose_name='Учебная группа')
    id_scholarship = models.IntegerField(null=True, blank=True, verbose_name='Код стипендии (1-4)')
    photo = models.ImageField(upload_to='students/%Y/%m/%d', null=True, blank=True, verbose_name='Фотография')

    def __str__(self):
        return f"{self.lastname} {self.firstname}"

    class Meta:
        db_table = 'student'
        verbose_name = 'Студент'
        verbose_name_plural = 'Студенты'


class DiplomaWork(models.Model):
    id_diploma = models.AutoField(primary_key=True)
    topic = models.CharField(max_length=100, verbose_name='Тема дипломной работы')
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column='id_student', verbose_name='Студент')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_column='id_teacher', verbose_name='Научный руководитель')

    def __str__(self):
        return str(self.topic)

    class Meta:
        db_table = 'diploma_work'
        verbose_name = 'Дипломная работа'
        verbose_name_plural = 'Дипломные работы'


class ExamSession(models.Model):
    id_exam = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, on_delete=models.DO_NOTHING, db_column='id_student', verbose_name='Студент')
    teacher = models.ForeignKey(Teacher, on_delete=models.DO_NOTHING, db_column='id_teacher', verbose_name='Преподаватель')
    discipline = models.ForeignKey(Discipline, on_delete=models.DO_NOTHING, db_column='id_discipline', verbose_name='Дисциплина')
    grade = models.IntegerField(verbose_name='Оценка')
    id_control_form = models.IntegerField(default=1, verbose_name='Код формы контроля')
    id_semester = models.IntegerField(default=1, verbose_name='Код семестра')

    def __str__(self):
        return f"{self.student} — {self.discipline}: {self.grade}"

    class Meta:
        db_table = 'exam_session'
        verbose_name = 'Экзаменационная ведомость'
        verbose_name_plural = 'Экзаменационная сессия'
