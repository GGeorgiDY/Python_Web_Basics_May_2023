# Generated by Django 4.2.1 on 2023-05-17 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='age',
            field=models.IntegerField(default=-1),
        ),
    ]
