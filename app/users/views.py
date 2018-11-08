# Create your views here.
from .models import User

# rest framework api.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers

# Create your views here.
class index(APIView):
    def get(self, request, format=None):
        try:
            user_list = User.objects.order_by('-birth_date')[:5]
        except models.User.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        serializer = serializers.UserSerializer(user_list, many=True, context={'request': request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)