from django.shortcuts import render
from rest_framework.response import Response
from .tasks import greet
from rest_framework.decorators import api_view

# Create your views here.

@api_view(['GET'])
def say_hello(request):
    # A function that takes in request 
    # logs the greet function into a message queue, waiting to be executed by the celery worker
    #  return a response 
    greet.delay()
    return Response({'result': 'it worked'})

