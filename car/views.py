from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Person , Car
from .serializers import PersonSer , CarSer , CarsReadSer
from rest_framework import viewsets , permissions
# Create your views here.

# @api_view(['GET' , 'POST'])
# def person_view(request)  :
#     if request.method == 'GET':
#         people = Person.objects.all()
#         return Response(PersonSer(people , many=True).data , status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         ser = PersonSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data , status=status.HTTP_201_CREATED)
#         else :
#             return Response(ser.errors , status = status.HTTP_400_BAD_REQUEST)

class PersonViewSet(viewsets.ModelViewSet):
    queryset = Person.objects.all()
    serializer_class = PersonSer
    http_method_names = ['get' , 'post' , 'put' , 'delete']

    search_fields = ('name' , )
    ordering_fields = '__all__'

    def list(self, request, *args, **kwargs):
        objs = super().list(request , *args, **kwargs)
        print("this is the list")
        return objs
    def create(self, request, *args, **kwargs):
        objs = super().create(request, *args, **kwargs)
        print("------create----")
        return objs

    def update(self, request, *args, **kwargs):
        objs = super().update(request, *args, **kwargs)
        instance = self.get_object()
        print("----update : {}".format(instance.name))
        return objs
    def retrieve(self, request, *args, **kwargs):
        objs = super().retrieve(request, *args, **kwargs)
        instance = self.get_object()
        print("----retrieve : {}".format(instance.name))
        return objs
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        print("----destroy : {}".format(instance.name))
        objs = super().destroy(request, *args, **kwargs)
        return objs


# @api_view(['GET' , 'POST'])
# def car_view(request)  :
#     if request.method == 'GET':
#         cars = Car.objects.all()
#         return Response(CarSer(cars , many=True).data , status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         ser = CarSer(data=request.data)
#         if ser.is_valid():
#             ser.save()
#             return Response(ser.data , status=status.HTTP_201_CREATED)
#         else :
#             return Response(ser.errors , status = status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET'])
# def info_view(request):
#     cars = Car.objects.all()
#     return Response(CarsReadSer(cars , many = True).data , status=status.HTTP_200_OK)

class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    http_method_names = ['get', 'post', 'put', 'delete']
    def get_serializer_class(self):
        if self.request.method not in permissions.SAFE_METHODS:
            return CarSer
        else :
            return CarsReadSer

