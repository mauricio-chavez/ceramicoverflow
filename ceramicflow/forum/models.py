from django.db import models
from generals.models import DefautlModel,  User

class Post(DefautlModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField( max_length=250,blank=False)
    likes = models.IntegerField()
    image = models.ImageField(null=True)

class Comments(DefautlModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=250,blank=False)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    likes = models.IntegerField()