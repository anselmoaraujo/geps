# Generated by Django 4.2 on 2023-04-19 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geps', '0008_estado_cidade_bairro'),
    ]

    operations = [
        migrations.CreateModel(
            name='showBairro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'Bairro',
            },
        ),
    ]
