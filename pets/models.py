from django.db import models


class Pet(models.Model):
    animal = models.CharField(max_length=35)
    breed = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    age = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} | {self.animal}"