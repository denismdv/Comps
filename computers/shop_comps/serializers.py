from rest_framework import serializers
from .models import Computers


class CompsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Computers
        fields = '__all__'