# Generated by Django 5.0.7 on 2024-08-07 02:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_rename_assignments_assignmentssubmissions_assignment_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='has_ended',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='session',
            name='has_started',
            field=models.BooleanField(default=False),
        ),
    ]
