# Generated by Django 5.0.7 on 2024-08-18 15:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_programme_session_count_schoolcalender'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='role',
        ),
        migrations.AddField(
            model_name='staff',
            name='roles',
            field=models.ManyToManyField(to='api.staffrole'),
        ),
    ]
