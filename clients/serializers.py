from rest_framework import serializers
from .models import Client


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['id', 'image', 'name', 'description', 'designation', 'created_at', 'updated_at']
        read_only_fields = ['id', 'created_at', 'updated_at']
       



