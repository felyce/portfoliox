# Generated by Django 3.0.4 on 2020-04-15 00:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('inovationapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='opinion',
            name='content',
            field=models.TextField(max_length=200),
        ),
        migrations.AlterField(
            model_name='opinion',
            name='goodcheck',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]