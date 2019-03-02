from django.db import models
from generals.models import DefautlModel, User
# Create your models here.
class Suppliers(DefautlModel):
    rating = models.DecimalField(max_digits=4, decimal_places=1)
    name = models.CharField(max_length=150, unique=True)
    description = models.CharField(max_length=250)

class Reviews(DefautlModel):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    supplier = models.ForeignKey(Suppliers, on_delete = models.CASCADE)
    rating = models.DecimalField(max_digits=2, decimal_places=1)
    comment = models.CharField(max_length=250)
    class Meta:
        verbose_name_plural = 'Reviews' 
        unique_together=(('user','supplier'))