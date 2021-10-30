from rest_framework.serializers import ModelSerializer
from .models import primary

class UserSerializer(ModelSerializer):
    class Meta:
        model=primary
        fields=['name','email','address']