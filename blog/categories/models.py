from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50)