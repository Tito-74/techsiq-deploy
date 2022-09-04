from django.db import models
from django.conf import settings
# Create your models here.
from cloudinary.models import CloudinaryField


class Category(models.Model):
  name = models.CharField(max_length=50)

  def __str__(self):
    return self.name



class Blog(models.Model):
  title = models.CharField(max_length=100, null=False, blank=False)
  body = models.TextField(max_length=350, null=False, blank=False)
  image = CloudinaryField('images')
  date_published = models.DateTimeField(auto_now_add=True,verbose_name='date_published')
  Author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  category = models.ForeignKey(Category, on_delete=models.CASCADE, default=None)

  def __str__(self):
    return self.title


class TechsiqTeam(models.Model):
  name = models.CharField(max_length=255)
  Title = models.CharField(max_length=100)
  social_media_link = models.URLField(max_length=255)
  detailsInfo = models.TextField(max_length=500)
  image = CloudinaryField('images')


  def __str__(self):
    return self.name

class CohortApplication(models.Model):
  applicant_name = models.CharField(max_length=255)
  email = models.EmailField(max_length=255)
  phone = models.CharField(max_length=255)
  module_type = models.CharField(max_length=255)

  def __str__(self):
    return self.applicant_name