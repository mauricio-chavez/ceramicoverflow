from django.db import models
from generals.models import DefautlModel, User

class Inventory(DefautlModel):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250)
    cost = models.DecimalField(max_digits=8,decimal_places=2)
    price = models.DecimalField(max_digits=8,decimal_places=2)
    aviable = models.BooleanField(default=True)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    image = models.ImageField(blank=True)

class Sales(DefautlModel):
    product = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False)
    
