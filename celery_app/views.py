from django.http import HttpResponse
from django.shortcuts import render
from .tasks import test_func,sleepy,student_data
# Create your views here.


def test(request):
    test_func.delay()
    return HttpResponse('function executed!')

def sleepy_func(request):
    sleepy.delay(10)
    return HttpResponse('Sleepy func executed!')


def Student_func(request):
    student_data.delay()
    return HttpResponse('Student_func Executed!')
