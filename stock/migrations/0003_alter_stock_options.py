# Generated by Django 4.1.3 on 2023-01-12 05:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stock', '0002_testproxy_alter_stock_category_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='stock',
            options={'verbose_name_plural': '在庫'},
        ),
    ]
