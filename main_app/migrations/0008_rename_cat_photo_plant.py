# Generated by Django 4.1.2 on 2022-10-12 02:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0007_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='photo',
            old_name='cat',
            new_name='plant',
        ),
    ]
