from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model
User=get_user_model()
# Create your models here.
class link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(blank= True, unique = True)
    author = models.ForeignKey(User, on_delete= models.CASCADE)
    created_date = models.DateTimeField()
    active = models.BooleanField(default = True)