# Generated by Django 3.0.8 on 2020-07-30 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0016_auto_20200730_2153'),
    ]

    operations = [
        migrations.AlterField(
            model_name='druginventory',
            name='cost_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True),
        ),
        migrations.AlterField(
            model_name='druginventory',
            name='selling_price',
            field=models.DecimalField(blank=True, decimal_places=2, default=0.0, max_digits=6, null=True),
        ),
    ]
