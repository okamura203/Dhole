from django.contrib.auth.models import User
from django.core import validators
from django.db import models
from django.urls import reverse


class Item(models.Model):
    name = models.CharField(
        verbose_name='名前',
        max_length=100,
    )

    unit_price = models.IntegerField(
        verbose_name='単価',
        validators=[validators.MinValueValidator(0)],
    )

    order = models.IntegerField(
        verbose_name='並び順',
        validators=[validators.MinValueValidator(0)],
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'メニュー'
        verbose_name_plural = 'メニュー'


class Invoice(models.Model):
    customer = models.PositiveSmallIntegerField(
        verbose_name='卓番',
    )

    sub_total = models.IntegerField(
        verbose_name='小計',
    )

    tax = models.IntegerField(
        verbose_name='消費税',
    )

    total_amount = models.IntegerField(
        verbose_name='合計金額',
    )

    created_at = models.DateTimeField(
        verbose_name='来店日時',
        auto_now_add=True
    )

    created_bt = models.DateTimeField(
        verbose_name='登録日',
        auto_now=True
    )

    def __str__(self):
        return str(self.customer)

    class Meta:
        verbose_name = '注文'
        verbose_name_plural = '注文'




class InvoiceDetail(models.Model):
    invoice = models.ForeignKey(
        Invoice,
        on_delete=models.CASCADE)

    item = models.ForeignKey(
        Item,
        verbose_name='商品',
        on_delete=models.CASCADE,
    )

    unit_price = models.IntegerField(
        verbose_name='単価',
        validators=[validators.MinValueValidator(0)],
    )

    quantity = models.IntegerField(
        verbose_name='数量',
        validators=[validators.MinValueValidator(0)],
    )

    amount = models.IntegerField(
        verbose_name='金額',
    )
