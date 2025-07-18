from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import responses, Response
from rest_framework import status
from rest_framework.status import HTTP_400_BAD_REQUEST

from .serializers import Calculator


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


# @api_view(['POST'])
# def calc(request):
#     try:
#         first_number = request.data['first_number']
#         second_number = request.data['second_number']
#         operation = request.data['operation']
#     except:
#         return Response({"error" : "send first and second number as well as operation"} , status=status.HTTP_400_BAD_REQUEST)
#     else :
#         if isinstance(first_number , int) and isinstance(second_number , int) :
#             if operation == "add" :
#                 return Response({"Result" : first_number + second_number} , status=status.HTTP_200_OK)
#             elif operation == "minus" :
#                 return Response({"Result" : first_number - second_number} , status= status.HTTP_200_OK)
#             elif operation == "multiply":
#                 return Response({"Result" : first_number * second_number} , status= status.HTTP_200_OK)
#             elif operation == "divide" :
#                 return Response({"Result" : first_number / second_number} , status= status.HTTP_200_OK)
#             else :
#                 return Response({"error" : "send a valid operation"} , status=status.HTTP_400_BAD_REQUEST)
#         else :
#             return Response({"error" : "first and second numbers should be integers"} ,
#                             status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def calc(request):
    ser = Calculator(data=request.data)

    if ser.is_valid():
        first_number = ser.validated_data['first_number']
        second_number = ser.validated_data['second_number']
        operation = ser.validated_data['operation']

        if operation == "add":
            result = first_number + second_number
        elif operation == "sub":
            result = first_number - second_number
        elif operation == "mul":
            result = first_number * second_number
        elif operation == "div":
            if second_number == 0:
                return Response({"error": "division by zero"}, status=status.HTTP_400_BAD_REQUEST)
            result = first_number / second_number
        else:
            return Response({"error": "Invalid operation"}, status=status.HTTP_400_BAD_REQUEST)

        return Response({"result": result}, status=status.HTTP_200_OK)

    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)