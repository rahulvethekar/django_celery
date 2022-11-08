from celery import shared_task
from time import sleep
from .models import Student

@shared_task(bind=True)
def test_func(self):
    for i in range(100):
        print(i)
    return 'completed!'

@shared_task(bind=True)
def sleepy(self,duration):
    sleep(duration)
    print('sleepy task completed!')
    return 'Done!'


@shared_task(bind=True)
def student_data(self):
    print('-----filling student Data!-----')
    sleep(15)
    Student(rn=10,name='vikas').save()
    return 'Student Data saved!'





