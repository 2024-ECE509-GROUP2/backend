# Generated by Django 5.0.7 on 2024-07-25 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_semester_date_end_alter_session_date_end'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='serial_no',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
