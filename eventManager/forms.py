from django.forms.models import ModelForm
from django import forms

from eventManager.models import *


class TeacherForm(ModelForm):
    #info about the class
    #teacherPassword=forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Teacher
        fields = ('teacherName',  'teacherPassword','teacherDept','teacherExperience')

class StudentForm(ModelForm):
    studentPassword = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model=Student
        fields=('studentRollNumber','studentName','studentPassword','studentDept','studentCGPA','studentAttendance')

class EventForm(ModelForm):
    class Meta:
        model=Event
        fields=('eventName','resourcePerson','eventDate','eventStartTime','eventEndTime','eventVenue','ECE','CSE','EEE','IT','mechanical','chemical','civil')


class Feedback(ModelForm):
    class Meta:
        model=Event
        fields=('eventRating',)


class RegisterStudent(ModelForm):
    class Meta:
        model = Student
        fields = ('studentName','studentRollNumber','studentPassword','studentDept','studentAttendance','studentCGPA')


class RegisterTeacher(ModelForm):
    class Meta :
        model = Teacher
        fields = ('teacherName','teacherPassword','teacherDept','teacherExperience')