from django.db import models

# Create your models here.
class Bloodbank(models.Model):
    name = models.CharField(max_length=255)
    mobile_number = models.IntegerField(null=True)
    age = models.IntegerField(null=True)
    blood_group = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    vol_of_blood = models.IntegerField(null=True)
    date = models.DateField(null=True)

    def __str__(self):
        return f"{self.name}"

