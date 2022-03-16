from django.db import models
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)
    image = models.ImageField(upload_to='blog/images/', blank=True)
    pub_date = models.DateField(auto_now=True)
    # url = models.URLField(blank=True)
    # blank=True is a property to make this optional so url is    optional
