# Generated by Django 3.0.3 on 2020-03-29 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0007_auto_20200329_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='img',
            field=models.ImageField(blank=True, upload_to='images/rooms'),
        ),
    ]