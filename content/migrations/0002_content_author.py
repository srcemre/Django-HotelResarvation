# Generated by Django 3.0.3 on 2020-05-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='author',
            field=models.CharField(blank=True, default='admin', max_length=255),
        ),
    ]
