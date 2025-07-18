from rest_framework import serializers

class Calculator(serializers.Serializer):
    first_number = serializers.IntegerField(required=True)
    second_number = serializers.IntegerField(required=True)
    operation = serializers.CharField(max_length=3)

