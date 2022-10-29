from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=35)
    adress = models.CharField(max_length=50)
    phone = models.IntegerField()
        
    def __str__(self) -> str:
        return f"{self.name} | {self.phone}"
