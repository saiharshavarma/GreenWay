# Generated by Django 3.2.6 on 2021-08-24 12:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogs', '0004_alter_blogplant_slug'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
