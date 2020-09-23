from django.shortcuts import render
from .models import *

# Create your views here.


def index(request):
    context = {
        'Classes': Classroom.objects.all()
    }
    return render(request, "index.html", context=context)


def classinfo(request):
    context = {
        'Students': Classroom.objects.get(roomNumber=request.GET['room-number']).students.all(),
    }
    return render(request, "class.html", context)


def studentinfo(request):
    context = {
        'Student': Student.objects.get(pk=request.GET['sid']),
        'Work': Student.objects.get(pk=request.GET['sid']).work.all(),
    }
    print(context['Work'])
    return render(request, "student.html", context)
