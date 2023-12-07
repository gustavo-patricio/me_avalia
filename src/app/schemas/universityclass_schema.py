from rest_framework import serializers
from app import models
from .classroom_schema import ClassroomSerializer 

class UniversityClassSerializer(serializers.ModelSerializer):
    classroom_id = ClassroomSerializer(read_only=True, write_only=False)
    class Meta:
        model = models.UniversityClass
        fields = ['uuid', 'inicio', 'final', 'classroom_id']

