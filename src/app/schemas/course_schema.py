from rest_framework import serializers
from app.models import Course

class CourseSerializers(serializers.ModelSerializer):

    class Meta:
        model = Course
        fields = ['uuid', 'name']