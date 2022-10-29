from django.db import models


class Location(models.Model):
    name = models.CharField(max_length=35)
    adress = models.CharField(max_length=50)
    n_hood = models.CharField(max_length=35)
        
    def __str__(self) -> str:
        return f"{self.full_name} | {self.id_num} | {self.pet_name}"
# Create your models here.
