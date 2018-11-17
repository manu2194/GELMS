# Generated by Django 2.1 on 2018-11-15 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0010_customuser_courses'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='courses',
            field=models.ManyToManyField(related_name='courses', to='courses.Course'),
        ),
    ]
