# Generated by Django 3.0.8 on 2020-07-23 05:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0006_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='staff',
            name='department',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stu.Department'),
        ),
    ]
