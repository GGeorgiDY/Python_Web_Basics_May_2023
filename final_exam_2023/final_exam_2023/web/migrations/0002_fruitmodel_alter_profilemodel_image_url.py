# Generated by Django 4.2.3 on 2023-07-24 21:38

import django.core.validators
from django.db import migrations, models
import final_exam_2023.web.models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FruitModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, validators=[django.core.validators.MinLengthValidator(2), final_exam_2023.web.models.validate_only_alphanumeric])),
                ('image_url', models.URLField()),
                ('description', models.TextField()),
                ('nutrition', models.CharField(blank=True, null=True)),
            ],
        ),
        migrations.AlterField(
            model_name='profilemodel',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
