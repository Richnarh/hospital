# Generated by Django 3.0.8 on 2020-07-19 11:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0004_auto_20200719_0352'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='staff',
            name='department',
        ),
        migrations.AlterField(
            model_name='patient',
            name='marital_status',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married'), ('SEPARATED', 'Separated'), ('WIDOWED', 'Widowed'), ('DIVORCED', 'Divorced'), ('NOT SPECIFIED', 'not specified')], default='NOT SPECIFIED', max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='gender',
            field=models.CharField(choices=[('MALE', 'Male'), ('FEMALE', 'Female'), ('NOT SPECIFIED', 'not specified')], default='NOT SPECIFIED', max_length=20),
        ),
        migrations.AlterField(
            model_name='staff',
            name='marital_status',
            field=models.CharField(choices=[('SINGLE', 'Single'), ('MARRIED', 'Married'), ('SEPARATED', 'Separated'), ('WIDOWED', 'Widowed'), ('DIVORCED', 'Divorced'), ('NOT SPECIFIED', 'not specified')], default='NOT SPECIFIED', max_length=50),
        ),
        migrations.AlterField(
            model_name='staff',
            name='title',
            field=models.CharField(choices=[('MR', 'Mr'), ('MRS', 'Mrs'), ('MS', 'Ms'), ('DR', 'Dr'), ('PROF.', 'Prof'), ('REV', 'Rev'), ('NOT SPECIFIED', 'not specified')], default='NOT SPECIFIED', max_length=50),
        ),
    ]
