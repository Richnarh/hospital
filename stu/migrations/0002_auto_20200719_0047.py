# Generated by Django 3.0.8 on 2020-07-19 00:47

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='department',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='staff',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
