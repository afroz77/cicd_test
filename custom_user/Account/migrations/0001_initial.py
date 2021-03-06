# Generated by Django 2.2.3 on 2019-08-21 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, default=None, max_length=255, null=True)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='Email Address')),
                ('username', models.CharField(default=None, max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='')),
                ('is_staff', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
