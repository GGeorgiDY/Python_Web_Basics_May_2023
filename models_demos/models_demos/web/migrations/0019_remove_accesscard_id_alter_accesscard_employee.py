# Generated by Django 4.2.1 on 2023-05-19 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0018_project_accesscard_employee_projects'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='accesscard',
            name='id',
        ),
        migrations.AlterField(
            model_name='accesscard',
            name='employee',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='web.employee'),
        ),
    ]