# Generated by Django 2.0.4 on 2023-02-03 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Folder', '0005_alter_account_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
