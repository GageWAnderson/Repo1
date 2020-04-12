from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#Profile extends the generic database model provided through django
class Profile(models.Model):
    #Cascade means that if the user in the database is
    #Deleted, also delete the profile
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # image = models.ImageField(default='default.jpg',upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    # def save(self, *args, **kwargs):
    #     #run save method of parent class first
    #     #Override the save method of the models.Model
    #     super().save(*args, **kwargs)

    #     #Grab the saved image and re-size it
    #     img = Image.open(self.image.path)
    #     if img.height > 300 or img.width > 300:
    #         output_size = (300,300)
    #         img.thumbnail(output_size)
    #         img.save(self.image.path)

#More memory efficiency could come from deleting old user images once they are updated