from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Person(models.Model):

    name = models.CharField(max_length=75)
    age = models.IntegerField(default=0)
    slug = models.SlugField(max_length=75, default=None)  # add_new
    created_time = models.DateTimeField(auto_now_add=True)

    banner = models.ImageField(default='fallback.jpg', blank=True)  # user's upload file

    # one user link many person .... in this case
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return self.name
