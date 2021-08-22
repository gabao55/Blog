# Generated by Django 3.2.6 on 2021-08-21 14:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('comments', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='comment',
            field=models.TextField(verbose_name='Comment:'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_email',
            field=models.EmailField(max_length=254, verbose_name='E-mail:'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_name',
            field=models.CharField(max_length=150, verbose_name='Name:'),
        ),
        migrations.AlterField(
            model_name='comments',
            name='comment_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
