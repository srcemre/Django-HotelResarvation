# Generated by Django 3.0.3 on 2020-05-15 07:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('content', '0003_auto_20200515_0832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='content',
            name='author',
        ),
        migrations.AddField(
            model_name='content',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='content',
            name='type',
            field=models.CharField(choices=[('menu', 'menu'), ('blog', 'blog'), ('agent', 'blog'), ('duyuru', 'duyuru'), ('etkinlik', 'etkinlik')], max_length=10),
        ),
    ]