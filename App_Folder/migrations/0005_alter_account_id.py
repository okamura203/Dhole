# Generated by Django 4.1 on 2023-02-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App_Folder', '0004_auto_20230131_1347'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
