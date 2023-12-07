from rest_framework import serializers
from app.models import Classroom
from .course_schema import CourseSerializers


class ClassroomSerializer(serializers.ModelSerializer):
    course = CourseSerializers(read_only=True, write_only=False)
    class Meta:
        model = Classroom
        fields = ['uuid','course']