# Generated by Django 3.0.8 on 2020-08-07 07:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stu', '0025_auto_20200807_0612'),
    ]

    operations = [
        migrations.RenameField(
            model_name='setuppassword',
            old_name='role_name',
            new_name='role',
        ),
    ]
