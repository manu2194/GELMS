# Generated by Django 2.1.3 on 2018-12-01 20:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tools', '0005_remove_tool_domain'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tool',
            name='course',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='course_tools', to='courses.Course'),
        ),
    ]
