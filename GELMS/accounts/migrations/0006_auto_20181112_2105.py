# Generated by Django 2.1 on 2018-11-13 02:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
        ('accounts', '0005_auto_20181112_1627'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='courses',
            field=models.ManyToManyField(to='courses.Course'),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='custom_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
