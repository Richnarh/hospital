# Generated by Django 3.0.8 on 2020-08-06 08:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0021_auto_20200806_0853'),
    ]

    operations = [
        migrations.RenameField(
            model_name='patient',
            old_name='patient_type',
            new_name='type_of_patient',
        ),
    ]
