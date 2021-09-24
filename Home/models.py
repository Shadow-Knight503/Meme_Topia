from django.db import models
from cloudinary.models import CloudinaryField


# Create your models here.
class Posts(models.Model):
    Title = models.CharField(max_length=500)
    Post = CloudinaryField('image')

    def __str__(self):
        return '{}'.format(self.Title)

    class Meta:
        verbose_name_plural = 'Posts'
