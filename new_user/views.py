from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework import status
from .permissions import IsOwner
from rest_framework.permissions import AllowAny , IsAuthenticated

from .serializers import User, UserSer


# Create your views here.

@api_view(['POST'])
@permission_classes((AllowAny , ))
def create_user(request):
    ser = UserSer(data=request.data)
    if ser.is_valid():
        ser.save()
        return Response(ser.data , status=status.HTTP_201_CREATED)
    else :
        return Response(ser.errors , status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes((IsAuthenticated , IsOwner))
def user_profile(request):
    try :
        user = User.objects.get(username=request.query_params['username'])
    except :
        return Response(status=status.HTTP_404_NOT_FOUND)

    ser = UserSer(user)
    return Response(ser.data , status=status.HTTP_200_OK)