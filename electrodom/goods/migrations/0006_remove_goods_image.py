# Generated by Django 4.2.3 on 2023-09-04 05:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0005_photo'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='goods',
            name='image',
        ),
    ]