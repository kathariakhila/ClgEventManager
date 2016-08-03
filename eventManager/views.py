from django.http.response import HttpResponse, JsonResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views.generic.base import View

from .models import*
from .serializers import *
from rest_framework import generics
from django.template import loader
from django.views.generic.list import ListView
from django.shortcuts import render,redirect
import json
from .forms import *
import pdb

from eventManager.models import *
from eventManager.serializers import *

class TeacherList(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer

class StudentList(generics.ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class EventDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer


#normal views
def index(request):
    template='eventManager/index.html'
    return render(request,template)

def TeacherLogin(request):
    template = 'eventManager/teacherLogin.html'
    return render(request, template)

class RegisterTeacher(View):

    form_class = RegisterTeacher
    template_name = 'eventManager/RegisterTeacher.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            teacher = form.save(commit=False)
            teacherName = form.cleaned_data['teacherName']
            teacherPassword = form.cleaned_data['teacherPassword']
            teacherDept = form.cleaned_data['teacherDept']
            teacherExperience = form.cleaned_data['teacherExperience']
            teacher.save()

            return redirect('/eventManager/teacherLogin/')


def AdminLogin(request):
    template='eventManager/adminLogin.html'
    return render(request,template)


def teacherLoginForm(request):
    if request.method == 'POST':
        if request.is_ajax():
            userName = request.POST.get('userName')
            password = request.POST.get('password')

            querySet=Teacher.objects.filter(teacherName=userName,teacherPassword=password)
            data=json.dumps([dict(item) for item in Teacher.objects.filter(teacherName=userName,teacherPassword=password).values('id','teacherName', 'teacherPassword')])

            return JsonResponse(data,safe=False)
    return render(request,'eventManager/teacherLoginForm.html')

def teacherLoggedIn(request,id):
    template = 'eventManager/index.html'
    return render(request, template)


def teacherOptions(request,pk):
    querySet = Event.objects.filter(id=pk)
    template = 'eventManager/teacherOptions.html'
    return render(request, template)

class CreateEvent(View):

    form_class = EventForm
    template_name = 'eventManager/eventForm.html'


    def get(self, request,id):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process data
    def post(self, request,id):
        form = self.form_class(request.POST)

        if form.is_valid():
            event = form.save(commit=False)
            eventName = form.cleaned_data['eventName']
            resourcePerson = form.cleaned_data['resourcePerson']
            eventVenue = form.cleaned_data['eventVenue']
            ECE = form.cleaned_data['ECE']
            CSE = form.cleaned_data['CSE']
            EEE = form.cleaned_data['EEE']
            IT = form.cleaned_data['IT']
            mechanical = form.cleaned_data['mechanical']
            chemical = form.cleaned_data['chemical']
            civil = form.cleaned_data['civil']
            eventDate = form.cleaned_data['eventDate']
            #eventDate = form.data.get('eventDate')
            eventStartTime = form.cleaned_data['eventStartTime']
            eventEndTime = form.cleaned_data['eventEndTime']
            t=Teacher.objects.filter(id=self.kwargs['id'])

            event.teacher=t[0]

            event.save()

            return redirect('/eventManager/teacherLogin/%i/' % int(id))


class viewMyEvents(ListView):
    model=Event
    template_name="eventManager/viewMyEvents.html"
    context_object_name="myEvents"

    def get_queryset(self):
        return Event.objects.filter(teacher_id=self.kwargs['id'])

class viewAllEvents(ListView):
    model=Event
    template_name="eventManager/viewAllEvents.html"
    context_object_name="allEvents"

    def get_queryset(self):
        return Event.objects.all()



class RegisterStudent(View):

    form_class = RegisterStudent
    template_name = 'eventManager/RegisterStudent.html'


    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            student = form.save(commit=False)
            studentName = form.cleaned_data['studentName']
            studentRollNumber = form.cleaned_data['studentRollNumber']
            studentPassword = form.cleaned_data['studentPassword']
            studentDept = form.cleaned_data['studentDept']
            studentCGPA = form.cleaned_data['studentCGPA']
            student.save()
            return redirect('/eventManager/studentLoginForm/studentLogin')

        else :
            return redirect('/eventManager/studentLoginForm/RegisterStudent')



def StudentLogin(request):
    if request.method == 'POST':
        if request.is_ajax():
            userName = request.POST.get('userName')
            password = request.POST.get('password')

            querySet = Teacher.objects.filter(teacherName=userName, teacherPassword=password)
            data = json.dumps([dict(item) for item in
                               Student.objects.filter(studentRollNumber=userName, studentPassword=password).values('id',
                                                                                                                   'studentName',
                                                                                                                   'studentPassword')])

            return JsonResponse(data, safe=False)

    return render(request, 'eventManager/studentLogin.html')





def StudentLoginForm(request):
    template = 'eventManager/StudentLoginForm.html'
    return render(request, template)



def studentOptions(request,pk):
    querySet = Event.objects.filter(id=pk)
    template = 'eventManager/studentOptions.html'
    context_object_name = "studentoptions"
    return render(request, template)

class viewMyDeptEvents(ListView):
    model=Event
    template_name="eventManager/viewMyDeptEvents.html"
    context_object_name="myEvents"

    def get_queryset(self):
        q=Student.objects.filter(id=self.kwargs['id']).values('studentDept')
        s=q[0].values()
        dept=s[0].encode('iso-8859-1')
        if(dept=='CSE' or dept == 'cse'):
            return Event.objects.filter(CSE=True)
        if (dept == 'ECE' or dept == 'ece'):
            return Event.objects.filter(ECE=True)
        if (dept == 'EEE' or dept == 'eee'):
            return Event.objects.filter(EEE=True)
        if (dept == 'IT' or dept == 'it'):
            return Event.objects.filter(IT=True)
        if (dept == 'mechanical' or dept == 'mech' or dept == 'MECH'):
            return Event.objects.filter(mechanical=True)
        if (dept == 'chemical' or dept == 'chem'):
            return Event.objects.filter(chemical=True)
        if (dept == 'civil' or dept == 'CIVIL'):
            return Event.objects.filter(civil=True)


class feedback(ListView):
    model = Event
    template_name = "eventManager/feedback.html"
    context_object_name = "myEvents"

    def get_queryset(self):

        s =Student.objects.filter(id = self.kwargs['id']).values('studentDept')
        a = s[0].values()
        dept = a[0].encode('iso-8859-1')

        if (dept == 'CSE' or dept == 'cse'):
            return Event.objects.filter(CSE=True)
        if (dept == 'ECE' or dept == 'ece'):
            return Event.objects.filter(ECE=True)
        if (dept == 'EEE' or dept == 'eee'):
            return Event.objects.filter(EEE=True)
        if (dept == 'IT' or dept == 'it'):
            return Event.objects.filter(IT=True)
        if (dept == 'mechanical' or dept == 'mech' or dept == 'MECH'):
            return Event.objects.filter(mechanical=True)
        if (dept == 'chemical' or dept == 'chem'):
            return Event.objects.filter(chemical=True)
        if (dept == 'civil' or dept == 'CIVIL'):
            return Event.objects.filter(civil=True)


class AddFeedback(View):

    form_class = Feedback
    template_name = 'eventManager/addfeedback.html'


    def get(self, request,id,eid):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process data
    def post(self, request,id,eid):
        form = self.form_class(request.POST)

        if form.is_valid():

            e = form.cleaned_data['eventRating']

            event = Event.objects.filter(id=self.kwargs['eid'])

            temp =event[0]

            if(temp.eventRating == 0):
                temp.eventRating = e

            else :
                temp.eventRating = (temp.eventRating+e)/2

            temp.save()

            return redirect('/eventManager/studentLoginForm/%i/' % int(id))




