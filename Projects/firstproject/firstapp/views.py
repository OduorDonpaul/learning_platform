from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404, render, redirect 
from datetime import date
from . models import Course, Lesson, Enrollment
from django.urls import reverse
from django.views import generic
from django.http import Http404

# Create your views here.

#def index(request):
  #  template = "<html>"\
   #             "This is your first view"\
    #            "</html>"

   # return HttpResponse(content=template)

def get_date(request):
    today = date.today()
    template = "<html>"\
                "Today's date is {}"\
                "<html>".format(today)
                
    return HttpResponse(content=template)

def popular_course_list(request):
    context = {}
    #if the request mathod is get
    if request.method == 'GET':
        #Using the objects model manage all course list
        #and sort them by total_enrollment descending
        course_list = Course.objects.order_by('-total_enrollment')[:10]
        #Appen the course list as an entry of context dict
        context['course_list'] = course_list
        return  render(request, 'firstapp/course_list.html', context)

def enroll(request, course_id):
    #if request is post
    if request.method == 'POST':
        #first try to read the course object
        #if could be found, raise a 404 exception
        course = get_object_or_404(Course, pk=course_id)
        #increase the enrollement by 1
        course.total_enrollment += 1
        course.save()
        #return a HttpResponse redirecting user to course list view
        return HttpResponseRedirect(reverse(viewname='firstapp:popular_course_list'))
