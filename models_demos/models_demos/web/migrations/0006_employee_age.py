# Generated by Django 4.2.1 on 2023-05-17 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0005_employee_level'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=19),
            preserve_default=False,
        ),
    ]
