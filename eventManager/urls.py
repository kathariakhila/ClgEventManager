from django.conf.urls import url, include
from . import views
from django.contrib import admin

app_name='eventManager'

urlpatterns=[
    #rest-api urls
    url(r'^teachers/$', views.TeacherList.as_view()),
    url(r'^students/$', views.StudentList.as_view()),
    url(r'^teachers/(?P<pk>[0-9]+)/$', views.EventDetail.as_view()),
    url(r'^students/(?P<pk>[0-9]+)/$', views.RegisteredEvents.as_view()),

    url(r'^$',views.index,name="index"),
    url(r'^teacherLogin/$',views.TeacherLogin,name="teacherLogin"),

    url(r'^teacherLogin/teacherLoginForm',views.teacherLoginForm,name="teacherLoginForm"),
    url(r'^teacherLogin/RegisterTeacher',views.RegisterTeacher.as_view(),name="RegisterTeacher"),

    url(r'^admin/adminLogin', views.AdminLogin, name="adminLogin"),

    url(r'^teacherLogin/(?P<pk>[0-9]+)/$', views.teacherOptions, name="teacherOptions"),
    url(r'^teacherLogin/(?P<id>[0-9]+)/createEvent/$', views.CreateEvent.as_view(), name="createEvent"),
    url(r'^teacherLogin/(?P<id>[0-9]+)/viewMyEvents/$', views.viewMyEvents.as_view(), name="viewMyEvents"),
    url(r'^teacherLogin/(?P<id>[0-9]+)/viewAllEvents/$', views.viewAllEvents.as_view(), name="viewAllEvents"),

    url(r'^studentLoginForm/$', views.StudentLoginForm, name="studentLoginForm"),
    url(r'^studentLoginForm/studentLogin$',views.StudentLogin,name="studentLogin"),
    url(r'^studentLoginForm/RegisterStudent',views.RegisterStudent.as_view(),name="RegisterStudent"),
    url(r'^studentLoginForm/(?P<pk>[0-9]+)/$', views.studentOptions, name="studentOptions"),
    url(r'^studentLoginForm/(?P<id>[0-9]+)/viewAllEvents/$', views.viewAllEvents.as_view(), name="viewAllEvents"),
    url(r'^studentLoginForm/(?P<id>[0-9]+)/viewMyDeptEvents/$', views.viewMyDeptEvents.as_view(), name="viewMyDeptEvents"),
    url(r'^studentLoginForm/(?P<id>[0-9]+)/registerEvent/$', views.registerEvent.as_view(), name="registerEvent"),

    url(r'^studentLoginForm/(?P<id>[0-9]+)/feedback/$', views.feedback.as_view(), name="feedback"),
    url(r'^studentLoginForm/(?P<id>[0-9]+)/feedback/(?P<eid>[0-9]+)/$',views.AddFeedback.as_view(),name = "AddFeedback")

]