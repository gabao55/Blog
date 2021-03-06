from django.db import models
from categories.models import Category
from django.contrib.auth.models import User
from django.utils import timezone
from PIL import Image
from django.conf import settings
import os

# Create your models here.
class Post(models.Model):
    post_tittle = models.CharField(max_length=255, verbose_name='Tittle')
    post_author = models.ForeignKey(User, on_delete=models.DO_NOTHING, verbose_name='Author')
    post_date = models.DateField(default=timezone.now, verbose_name='Date of publishment')
    post_content = models.TextField(verbose_name='Content')
    post_excerpt = models.TextField(verbose_name='Excerpt')
    post_category = models.ForeignKey(Category, on_delete=models.DO_NOTHING, blank=True, null=True, verbose_name='Category')
    post_image = models.ImageField(upload_to='post_img/%Y/%m/%d', blank=True, null=True, verbose_name='Image')
    post_published = models.BooleanField(default=False, verbose_name='Is published')

    def __str__(self):
        return self.post_tittle

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        self.resize_image(self.post_image, 800)
    
    @staticmethod
    def resize_image(img_name, new_width):
        try:
            img_path = os.path.join(settings.MEDIA_ROOT, str(img_name))
            img = Image.open(img_path)
            width, height = img.size
            new_height = round((new_width * height) / width)

            if width <= new_width:
                img.close()
                return

            new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
            new_img.save(
                img_path,
                optimize=True,
                quality=60
            )
        except:
            pass