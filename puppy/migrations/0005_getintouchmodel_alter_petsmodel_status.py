# Generated by Django 4.1.2 on 2022-11-24 07:57

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('puppy', '0004_petsmodel_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='GetInTouchModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('message', models.TextField(max_length=300, validators=[django.core.validators.MinLengthValidator(1)])),
                ('name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(1)])),
                ('email', models.EmailField(max_length=80, validators=[django.core.validators.MinLengthValidator(1)])),
                ('subject', models.CharField(max_length=100, validators=[django.core.validators.MinLengthValidator(1)])),
            ],
        ),
        migrations.AlterField(
            model_name='petsmodel',
            name='status',
            field=models.CharField(choices=[('N', 'Need help'), ('T', 'Now on therapy'), ('H', 'Healthy')], default='H', max_length=1),
        ),
    ]