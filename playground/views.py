from django.shortcuts import render
<<<<<<< HEAD
from .task import notify_customer

def say_hello(request):
    notify_customer.delay('Hello')
=======


def say_hello(request):
>>>>>>> 0034254 (all added)
    return render(request, 'hello.html', {'name': 'Mosh'})
