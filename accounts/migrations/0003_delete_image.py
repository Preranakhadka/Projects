# Generated by Django 3.2 on 2021-09-01 16:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_image_id'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Image',
        ),
    ]