from django.db import models
from django.contrib.auth.models import AbstractUser
from pyparsing import FollowedBy

from apps.managers import TeacherManager
from apps.constants import GENDAR
# Create your models here.

class Class(models.Model):
    title = models.CharField(max_length=255, verbose_name='Класс')
    teacher = models.OneToOneField('Teacher', related_name='teacher_class', on_delete=models.SET_NULL, blank=True, null=True,verbose_name='Учитель')


    def __str__(self) -> str:
        return self.title

class Student(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    birthday = models.DateField()
    address = models.CharField(max_length=355)
    gendar = models.CharField(choices=GENDAR, max_length=255)
    group = models.ForeignKey(Class, related_name='class_student', on_delete=models.SET_NULL, blank=True, null=True, verbose_name='Класс')

    def __str__(self) -> str:
        return self.name


class Teacher(AbstractUser):
    email = None
    username = None
    phone_number = models.CharField(max_length=255, unique=True, verbose_name='Номер телефона')

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []

    objects = TeacherManager()

    def __str__(self):
        return self.phone_number
