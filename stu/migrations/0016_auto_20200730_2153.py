# Generated by Django 3.0.8 on 2020-07-30 21:53

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0015_auto_20200727_2112'),
    ]

    operations = [
        migrations.AddField(
            model_name='druginventory',
            name='cost_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='druginventory',
            name='selling_price',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.CreateModel(
            name='Billing',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('nhis_available', models.BooleanField(default=False)),
                ('nhis_number', models.CharField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('drug', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stu.DrugInventory')),
                ('patient', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='stu.Patient')),
            ],
        ),
    ]