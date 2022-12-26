from rest_framework import serializers
from .models import *


class EmployeeSerializer(serializers.ModelSerializer):
    manager = serializers.CharField(read_only=True)

    class Meta:
        model = Employee
        fields = ['id', 'name', 'role', 'salary', 'manager']
