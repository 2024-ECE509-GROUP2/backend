# Generated by Django 5.0.7 on 2024-08-13 14:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_session_programme'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='programme',
            field=models.ForeignKey(default='e5c89744-b04e-41bd-9a44-81dd306d790f', on_delete=django.db.models.deletion.PROTECT, to='api.programme'),
            preserve_default=False,
        ),
    ]
