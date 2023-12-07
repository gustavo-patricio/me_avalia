from django.db import models
import uuid

from .course_model import Course
from .teacher_model import Teacher

class Classroom(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='classrom')
    semester = models.CharField(max_length=6)
    teacher = models.ForeignKey(Teacher, on_delete=models.SET_NULL, null=True)

    class Meta:
        verbose_name_plural= "turma"

    def __str__(self) -> str:
        return f"{self.course.name}, {self.semester}"