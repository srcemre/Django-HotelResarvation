# Generated by Django 3.0.3 on 2020-05-18 11:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0010_auto_20200518_1356'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='ordernumber',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]