# Generated by Django 4.1.7 on 2023-03-29 23:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('functional', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
