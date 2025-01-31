# Generated by Django 3.0.3 on 2020-03-29 12:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accommodation', '0006_auto_20200328_1817'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='image',
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/categorys'),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='title',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='room',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/rooms'),
        ),
        migrations.AlterField(
            model_name='room',
            name='title',
            field=models.CharField(max_length=150),
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('image', models.ImageField(blank=True, upload_to='images/rooms')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='accommodation.Hotel')),
            ],
        ),
    ]
