from rest_framework import serializers
from . import models

class UserSerializer(serializers.ModelSerializer):
    birth_date = serializers.ReadOnlyField()
    gender = serializers.ReadOnlyField()
    
    class Meta:
        model = models.User
        fields = (
            'username',
            'email',
            'birth_date',
            'gender',
        )
