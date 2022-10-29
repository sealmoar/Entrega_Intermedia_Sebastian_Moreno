from django.db import models


class Service(models.Model):
    name = models.CharField(max_length=35)
    price = models.IntegerField()
        
    def __str__(self) -> str:
        return f"{self.service_name} | {self.price}"
# Create your models here.
