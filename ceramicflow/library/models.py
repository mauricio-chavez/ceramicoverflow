from django.db import models
from generals.models import User, DefautlModel

class Library(DefautlModel):
    book = models.FileField(upload_to='/books')
    user  = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=150)