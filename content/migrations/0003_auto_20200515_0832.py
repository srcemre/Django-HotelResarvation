# Generated by Django 3.0.3 on 2020-05-15 05:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('content', '0002_content_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('menu', 'menu'), ('blog', 'blog'), ('duyuru', 'duyuru'), ('etkinlik', 'etkinlik')], max_length=10),
        ),
    ]
