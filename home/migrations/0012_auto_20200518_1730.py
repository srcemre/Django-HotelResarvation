# Generated by Django 3.0.3 on 2020-05-18 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0011_faq_ordernumber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='settings',
            name='icon',
            field=models.ImageField(blank=True, upload_to='images/settings/icon'),
        ),
    ]
