from django.urls import path
from .views import test,sleepy_func,Student_func
urlpatterns =[
    path('test/',test, name='test'),
    path('sleepy/',sleepy_func),
    path('stu/',Student_func),
]