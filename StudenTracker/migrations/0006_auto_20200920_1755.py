# Generated by Django 3.1.1 on 2020-09-20 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('StudenTracker', '0005_auto_20200920_1718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='Class',
        ),
        migrations.AddField(
            model_name='student',
            name='work',
            field=models.ManyToManyField(to='StudenTracker.Assignment'),
        ),
    ]