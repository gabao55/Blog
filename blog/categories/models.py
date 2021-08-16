from django.db import models

# Create your models here.
class Category(models.Model):
    cat_name = models.CharField(max_length=50)

    def __str__(self):
        return self.cat_name