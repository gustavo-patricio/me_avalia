from django.db  import models
import uuid
from django.utils import timezone
from .classroom_model import Classroom

class UniversityClass(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    classroom_id = models.ForeignKey(Classroom, on_delete=models.CASCADE, related_name='universityclasses')
    inicio = models.DateTimeField()
    final = models.DateTimeField()

    
    class Meta:
        ordering = ["-inicio"]
        verbose_name_plural= "aula"

    def __str__(self) -> str:
        return f"{self.uuid}, {self.inicio}, {self.final}, {self.classroom_id}"
