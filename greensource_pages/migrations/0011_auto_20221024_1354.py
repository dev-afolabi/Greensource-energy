# Generated by Django 3.0.3 on 2022-10-24 12:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('greensource_pages', '0010_landingpage'),
    ]

    operations = [
        migrations.RenameField(
            model_name='landingpage',
            old_name='name',
            new_name='title',
        ),
    ]