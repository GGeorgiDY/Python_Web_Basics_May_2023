# Generated by Django 4.2.4 on 2023-08-15 00:18

import django.core.validators
from django.db import migrations, models
import exam_june_2023.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fruit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fruit_name', models.CharField(max_length=30, validators=[django.core.validators.MinLengthValidator(2), exam_june_2023.web.models.validate_fruit_name_contains_only_letters])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='password',
            field=models.CharField(max_length=20, validators=[django.core.validators.MinLengthValidator(8)]),
        ),
    ]