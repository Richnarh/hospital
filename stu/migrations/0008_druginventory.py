# Generated by Django 3.0.8 on 2020-07-23 06:33

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0007_staff_department'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrugInventory',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('drug_name', models.CharField(blank=True, max_length=100, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('date', models.DateField(blank=True, null=True)),
                ('remark', models.CharField(blank=True, max_length=255, null=True)),
                ('signatory', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='stu.Staff')),
            ],
        ),
    ]