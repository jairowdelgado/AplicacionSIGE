from django.db import models

# Create your models here.
class Electiva(models.Model):
    code = models.CharField(max_length=20)    
    name = models.CharField(max_length=140)

    class Meta:
        db_table='electivas'

    def __str__(self):
        return self.name
