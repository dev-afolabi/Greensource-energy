# Generated by Django 3.0.3 on 2022-10-24 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greensource_pages', '0013_remove_landingpage_pics'),
    ]

    operations = [
        migrations.AddField(
            model_name='landingpage',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
    ]
