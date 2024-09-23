from django.db import models
from django.core.exceptions import ValidationError
# Create your models here.

def alphaneumeric(value):
    if not str(value).isalnum():
        raise ValidationError("Only alphabets and Number are allowed")
    return value

class Showroomlist(models.Model):
    name = models.CharField(max_length=30)
    location = models.CharField(max_length=100)
    website = models.URLField(max_length=100)

    def __str__(self):
        return self.name
    
class Carlist(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    active = models.BooleanField(default=False)
    chassisnumber = models.CharField(max_length=100, blank=True, null=True)
    price = models.DecimalField(max_digits=9,decimal_places=2, blank=True, null=True)
    showroom = models.ForeignKey(Showroomlist, on_delete = models.CASCADE, related_name = 'Showrooms',null = True)  

    def __str__(self):
        return f"{self.name}\n{self.chassisnumber if self.chassisnumber else 'No Chassis Number'}"