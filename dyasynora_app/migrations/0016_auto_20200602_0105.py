# Generated by Django 3.0.6 on 2020-06-02 01:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dyasynora_app', '0015_project_org_desc'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='dislikes',
            new_name='supporters',
        ),
        migrations.RemoveField(
            model_name='project',
            name='likes',
        ),
    ]
