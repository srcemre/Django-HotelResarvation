# Generated by Django 3.0.3 on 2020-03-29 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Settings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=255)),
                ('address', models.TextField(blank=True, max_length=255)),
                ('phone', models.CharField(blank=True, max_length=255)),
                ('fax', models.CharField(blank=True, max_length=255)),
                ('email', models.CharField(blank=True, max_length=255)),
                ('smtpserver', models.CharField(max_length=20)),
                ('smtpemail', models.CharField(max_length=20)),
                ('smtppassword', models.CharField(max_length=10)),
                ('smtpport', models.CharField(max_length=5)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(max_length=50)),
                ('instagram', models.CharField(max_length=50)),
                ('twitter', models.CharField(max_length=50)),
                ('aboutus', models.TextField()),
                ('references', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
