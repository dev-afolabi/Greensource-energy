# Generated by Django 3.0.3 on 2021-09-09 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greensource_pages', '0030_auto_20210831_1827'),
    ]

    operations = [
        migrations.CreateModel(
            name='Testimonial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('title', models.CharField(max_length=100)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('date', models.DateField(auto_now_add=True)),
                ('body', models.TextField()),
            ],
            options={
                'ordering': ['-date'],
                'get_latest_by': 'date',
            },
        ),
    ]
