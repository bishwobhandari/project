from django.db import models

# Create your models here.


class TaxRates(models.Model):
    state= models.CharField(max_length=20)
    state_code=models.CharField(max_length=2)
    tax_rate=models.FloatField()
    image=models.ImageField(blank=True, null=True)

    def __str__(self):   
        return self.state


