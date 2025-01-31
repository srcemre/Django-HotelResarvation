# Generated by Django 3.0.3 on 2020-03-29 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0010_auto_20200329_1621'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image',
        ),
        migrations.RemoveField(
            model_name='hotel',
            name='img',
        ),
        migrations.RemoveField(
            model_name='room',
            name='image',
        ),
        migrations.AddField(
            model_name='category',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/null.jpg', upload_to='images/categorys'),
        ),
        migrations.AddField(
            model_name='hotel',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/null.jpg', upload_to='images'),
        ),
        migrations.AddField(
            model_name='room',
            name='thumbnail',
            field=models.ImageField(blank=True, default='images/null.jpg', upload_to='images/rooms'),
        ),
        migrations.AlterField(
            model_name='image',
            name='image',
            field=models.ImageField(blank=True, default='images/null.jpg', upload_to='images'),
        ),
    ]
