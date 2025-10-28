from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Employee
from .serializers import EmployeeSer

# Create your views here.

@api_view(['POST'])
def post_employee(request):
    data = {
        'name' : request.data['name'] ,
        'age' : request.data['age'],
        'salary': request.data['salary'],
        'position': request.data['position'],
    }
    ser = EmployeeSer(data=data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data , status = status.HTTP_201_CREATED)
    else :
        return Response(ser.errors , status= status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def list_employees(request):
    employees = Employee.objects.all()
    ser = EmployeeSer(employees , many=True)
    return Response(ser.data , status = status.HTTP_200_OK)

@api_view(['PUT' , 'GET' , 'DELETE'])
def get_update_delete_employee(request , pk):
    try:
        employee = Employee.objects.get(pk=pk)
    except:
        return Response({'error' : 'not found'} , status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'GET':
        ser = EmployeeSer(employee)
        return Response(ser.data , status= status.HTTP_200_OK)
    elif request.method == 'PUT':
        ser = EmployeeSer(employee , data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data , status= status.HTTP_200_OK)
        else :
            return Response(ser.errors , status= status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        employee.delete()
        return Response(status= status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def search_employee(request):
    employees = Employee.objects.filter(name=request.query_params['name'])
    if employees:
        ser = EmployeeSer(employees , many=True)
        return Response(ser.data , status=status.HTTP_200_OK)
    else:
        return Response(status=status.HTTP_200_OK)



