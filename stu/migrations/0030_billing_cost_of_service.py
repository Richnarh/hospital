# Generated by Django 3.0.8 on 2020-08-09 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0029_auto_20200808_1327'),
    ]

    operations = [
        migrations.AddField(
            model_name='billing',
            name='cost_of_service',
            field=models.FloatField(blank=True, help_text='NOTE: for non student only', null=True),
        ),
    ]
