# Generated by Django 3.0.3 on 2020-05-14 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20200514_2153'),
    ]

    operations = [
        migrations.AddField(
            model_name='reservationroom',
            name='checkin',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationroom',
            name='checkout',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='reservationroom',
            name='person',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]