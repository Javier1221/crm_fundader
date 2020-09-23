from django.shortcuts import render
from course.models import areasCurso
from django.http import HttpResponse
# Create your views here.



def areas(request):
    area =  areasCurso.objects.all()

    context= {'area':area}

    return  render(request ,'course/areas.html' , context)
