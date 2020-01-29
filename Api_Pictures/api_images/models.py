from django.db import models

# Create your models here.

class Picture(models.Model):
    file = models.ImageField(upload_to='pictures')
    name = models.TextField(max_length=30)

    @classmethod
    def create(cls, file=None, name='Unnamed'):
        picture = cls(file=file, name=name)
        return picture