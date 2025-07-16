from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import responses, Response


# Create your views here.

@api_view()
def index(request):
    return Response({'message' : 'hello , world'})


@api_view(['GET' , 'POST'])
def hello(request):
    if request.method == "GET":
        return Response({'message' : 'hellow world!'})
    elif request.method == "POST":
        return Response({"message" : "Hello , {}".format(request.data['name'])})
