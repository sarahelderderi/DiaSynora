# Generated by Django 2.2.6 on 2019-11-06 17:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0004_project_project_img'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_cost',
            field=models.IntegerField(default=0),
        ),
    ]
