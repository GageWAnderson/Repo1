from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

#Post, but called something different
class Build(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField() #Unrestricted text
    data_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    matchup = models.CharField(max_length=3) #How to select between 9 options here?

    def __str__(self):
        return self.title

        