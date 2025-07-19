from rest_framework import serializers
from .models import Person , Car

class PersonSer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = '__all__'


class CarSer(serializers.ModelSerializer):
    class Meta:
        model = Car
        fields = '__all__'

class CarsReadSer(serializers.ModelSerializer):
    person = PersonSer()
    class Meta:
        model = Car
        fields = '__all__'
        # depth = 1