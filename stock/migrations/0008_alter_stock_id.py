# Generated by Django 4.1 on 2023-02-03 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0007_auto_20230203_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='stock',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
