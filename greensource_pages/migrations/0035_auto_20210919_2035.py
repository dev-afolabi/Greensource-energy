# Generated by Django 3.0.3 on 2021-09-19 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greensource_pages', '0034_solar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solar',
            name='slug',
            field=models.SlugField(default='', unique=True),
            preserve_default=False,
        ),
    ]
