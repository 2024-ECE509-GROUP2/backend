# Generated by Django 5.0.7 on 2024-08-13 14:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0012_session_has_ended_session_has_started'),
    ]

    operations = [
        migrations.AddField(
            model_name='session',
            name='programme',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='api.programme'),
        ),
    ]
