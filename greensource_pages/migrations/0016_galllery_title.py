# Generated by Django 3.0.3 on 2021-08-31 00:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greensource_pages', '0015_galllery_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='galllery',
            name='title',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
