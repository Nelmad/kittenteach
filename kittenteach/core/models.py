from django.contrib.auth.models import User
from django.db import models

from django.db.models import CASCADE, SET_NULL, PROTECT


class Subject(models.Model):
    name = models.CharField(max_length=255, unique=True)

    class Meta:
        db_table = 'subjects'


class Student(models.Model):
    user = models.OneToOneField(User, on_delete=PROTECT)

    class Meta:
        db_table = 'students'


class Teacher(models.Model):
    user = models.OneToOneField(User, on_delete=PROTECT)
    students = models.ManyToManyField(Student, related_name='teachers', blank=True)
    subjects = models.ManyToManyField(Subject, related_name='subjects', blank=True)

    class Meta:
        db_table = 'teachers'


class Group(models.Model):
    name = models.CharField(max_length=255)
    teacher = models.ForeignKey(Teacher, on_delete=CASCADE)
    subject = models.ForeignKey(Subject, null=True, on_delete=SET_NULL)
    students = models.ManyToManyField(Student)

    class Meta:
        db_table = 'groups'


class LessonTemplate(models.Model):
    # set lessons for schedule
    group = models.ForeignKey(Group, on_delete=CASCADE)
    weekday = models.IntegerField()
    time = models.TimeField()

    class Meta:
        db_table = 'lessons_templates'


class Lesson(models.Model):
    group = models.ForeignKey(Group, on_delete=CASCADE)
    date = models.DateTimeField()  # not current time -> wrap LessonTemplate weekday and time

    class Meta:
        db_table = 'lessons'


class Attendance(models.Model):
    lesson = models.ForeignKey(Lesson, on_delete=CASCADE)
    student = models.ForeignKey(Student, on_delete=CASCADE)
    attended = models.BooleanField()

    class Meta:
        db_table = 'attendance'


class Balance(models.Model):
    balance = models.IntegerField()
    student = models.ForeignKey(Student, on_delete=PROTECT)
    teacher = models.ForeignKey(Teacher, on_delete=PROTECT)

    class Meta:
        db_table = 'balance'


class Payment(models.Model):
    amount = models.PositiveIntegerField()
    type = models.CharField(max_length=1, choices=((0, 'deposit'), (1, 'withdraw')))
    current_balance = models.IntegerField()

    lesson = models.ForeignKey(Lesson, null=True, on_delete=PROTECT)

    balance = models.ForeignKey(Balance, on_delete=PROTECT)
    date = models.DateTimeField(auto_now_add=True)  # auto set current date at the moment of payment add

    class Meta:
        db_table = 'payments'
