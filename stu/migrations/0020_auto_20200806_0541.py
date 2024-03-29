# Generated by Django 3.0.8 on 2020-08-06 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0019_auto_20200806_0504'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='patient_id',
            field=models.CharField(blank=True, max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='patient_type',
            field=models.CharField(choices=[('STUDENT', 'Student'), ('NON_STUDENT', 'Non Student'), ('NOT SPECIFIED', 'not specified')], default='NOT SPECIFIED', max_length=100),
        ),
    ]
