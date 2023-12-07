from django.db import models
import uuid

class Teacher(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4(),
                            editable=False)
    name = models.CharField(max_length=150)
    registration_number = models.CharField(unique=True, max_length=8)

    class Meta:
        verbose_name_plural= "professor"


    def __str__(self) -> str:
        return f"{self.uuid}, {self.name}, {self.registration_number}"