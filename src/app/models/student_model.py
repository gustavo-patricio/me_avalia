from django.db import models
from django.contrib.auth.models import User
import uuid

class Student(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4(),
                            editable=False)
    
    name = models.CharField(max_length=150)
    registration_number = models.CharField(max_length=8)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="student")
    class Meta:
        verbose_name_plural= "aluno"



    def __str__(self) -> str:
        return f"{self.uuid}, {self.name}, {self.registration_number}"

