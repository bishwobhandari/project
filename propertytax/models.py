from django.db import models

# Create your models here.


class PropertyTax(models.Model):
    state= models.CharField(max_length=20)
    state_code=models.CharField(max_length=2)
    property_tax=models.FloatField()

    def __str__(self):   
        return self.state


