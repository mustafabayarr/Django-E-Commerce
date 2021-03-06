# Generated by Django 3.1.7 on 2021-03-28 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('keywords', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
                ('company', models.CharField(max_length=50)),
                ('address', models.CharField(blank=True, max_length=150)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('fax', models.CharField(blank=True, max_length=15)),
                ('email', models.CharField(blank=True, max_length=55)),
                ('smtpserver', models.CharField(blank=True, max_length=30)),
                ('smtpemail', models.CharField(blank=True, max_length=30)),
                ('smtppassword', models.CharField(blank=True, max_length=30)),
                ('smtpport', models.CharField(blank=True, max_length=30)),
                ('icon', models.ImageField(blank=True, upload_to='images/')),
                ('facebook', models.CharField(blank=True, max_length=30)),
                ('instagram', models.CharField(blank=True, max_length=30)),
                ('youtube', models.CharField(blank=True, max_length=30)),
                ('twitter', models.CharField(blank=True, max_length=30)),
                ('aboutus', models.TextField()),
                ('contact', models.TextField()),
                ('references', models.TextField()),
                ('status', models.CharField(choices=[('True', 'Evet'), ('False', 'Hayır')], max_length=10)),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
