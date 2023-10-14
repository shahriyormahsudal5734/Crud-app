from django.db import models
from django.contrib.auth.models import User
import datetime

class Category(models.Model):
    title = models.CharField(max_length=200)
    time = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=20)
    def __str__(self):
        return self.title


class Post(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    img = models.ImageField(upload_to='img/')
    vaqti = models.CharField(max_length=200,default=datetime.date.today)
    categ = models.ForeignKey(Category,on_delete=models.CASCADE,default=1)
    user = models.CharField(max_length=200)
    def __str__(self):
        return self.title
    class Meta:
        ordering = ('-id','-id')

JINS = (
    ('Erkak','Erkak'),
    ('Ayol','Ayol'),
)
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE,auto_created=True)
    image = models.ImageField( upload_to='profiles/' )
    bio = models.TextField()
    jinsi = models.CharField(choices=JINS,max_length=100)
    ages = models.IntegerField()
    numberphone = models.IntegerField(default='998')
    def __str__(self):
        return str( self.user.username)

