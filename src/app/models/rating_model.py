from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone 

import uuid
from datetime import datetime
from .student_model import Student
from .universityclass_model import UniversityClass


class Rating(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    score = models.IntegerField(validators=[
            MaxValueValidator(5, message="O valor deve ser menor ou igual a 5."),
            MinValueValidator(1, message="O valor deve ser maior ou igual a 1."),
    ])
    feedback = models.TextField(blank=True)
    date_created = models.DateTimeField(default=timezone.datetime.today(), editable=False)
    students = models.ForeignKey(Student, related_name='ratings', on_delete=models.CASCADE)
    universityclass = models.ForeignKey(UniversityClass, on_delete=models.CASCADE, related_name='rating')
    
    class Meta:
        verbose_name_plural= "avaliações"
        unique_together = ('students', 'universityclass')


    def __str__(self) -> str:
        return f"{self.uuid}, {self.score}, {self.feedback}, {self.date_created}"

