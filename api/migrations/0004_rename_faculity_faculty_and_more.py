# Generated by Django 5.0.7 on 2024-07-23 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_assignmentsassigned_uuid_and_more'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Faculity',
            new_name='Faculty',
        ),
        migrations.RenameField(
            model_name='department',
            old_name='faculity',
            new_name='faculty',
        ),
        migrations.RenameField(
            model_name='faculty',
            old_name='faculity_name',
            new_name='faculty_name',
        ),
    ]
