from rest_framework import serializers
from Tasks.models import *
class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        field = '__all__'

