# Generated by Django 3.0.3 on 2020-05-13 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_userprofile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='images/users/user.png', upload_to='images/users/'),
        ),
    ]
