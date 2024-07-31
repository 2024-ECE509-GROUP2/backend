# Generated by Django 5.0.7 on 2024-07-26 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_student_serial_no'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='serial_no',
            new_name='student_id',
        ),
        migrations.AddField(
            model_name='department',
            name='department_code',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staff',
            name='staff_id',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='staffrole',
            name='role_code',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
