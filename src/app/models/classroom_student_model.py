from django.db import models
import uuid

from .student_model import Student
from .classroom_model import Classroom

class ClassroomStudent(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4(), 
                            editable=False)
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE, related_name='classrooms')
    classroom_id = models.ForeignKey(Classroom, models.CASCADE)

    class Meta:
        verbose_name_plural= "atribuir turma ao aluno"
        unique_together = ('student_id', 'classroom_id')
    

