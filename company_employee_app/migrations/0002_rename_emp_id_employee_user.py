# Generated by Django 4.0.2 on 2022-02-27 09:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company_employee_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emp_id',
            new_name='user',
        ),
    ]
