# Generated by Django 4.1.3 on 2022-11-28 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='stock',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=100, verbose_name='カテゴリー名')),
                ('item_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='商品名')),
                ('inventory', models.PositiveIntegerField(blank=True, null=True, verbose_name='在庫数')),
                ('created_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
