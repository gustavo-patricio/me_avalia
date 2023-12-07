from django.db import models
import uuid

class Course(models.Model):
    uuid = models.UUIDField(primary_key=True,
                            default=uuid.uuid4(),
                            editable=False)
    name = models.CharField(unique=True)

    class Meta:
        verbose_name_plural= "disciplina"



    def __str__(self) -> str:
        return self.name