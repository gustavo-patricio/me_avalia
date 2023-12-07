from rest_framework import serializers
from app import models
from .ratings_schema import RatingSerializer


class ClassroomStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ClassroomStudent
        fields = ['classroom_id']

class StudentSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True, write_only=False)
    class Meta:
        model = models.Student
        fields = ['uuid', 'name', 'registration_number', 'ratings']


    


