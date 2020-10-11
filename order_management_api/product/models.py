from django.db import models

from config.models import AbstractCreateUpdateModel, AbstractBigIntPkModel

from users.models import UserProfile


class Product(AbstractBigIntPkModel):
    class Meta(AbstractBigIntPkModel.Meta):
        db_table = 'products'

    name = models.CharField(max_length=32, db_index=True)
    price = models.BigIntegerField(null=False, default=0)
    discount = models.BigIntegerField(null=False, default=0)


class Order(AbstractCreateUpdateModel):
    class Meta(AbstractCreateUpdateModel.Meta):
        db_table = 'orders'

    NEW = 0
    COMPLETED = 1
    PAID = 2
    CANCELED = 3

    STATUS_CHOICES = (
        (NEW, 'New'),
        (COMPLETED, 'Completed'),
        (PAID, 'Paid'),
        (CANCELED, 'Canceled')
    )

    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    status = models.SmallIntegerField(
        choices=STATUS_CHOICES, null=False, db_index=True, default=0
    )
    # cashier_id - For history. Which cashier created the order.
    # Required field. Written after created
    cashier = models.ForeignKey(
        UserProfile, null=False, related_name='cashier',
        on_delete=models.CASCADE
    )
    # shop_assistant_id - For history. Which shop assistant processed order.
    # Updated before the status changes to Completed.
    shop_assistant = models.ForeignKey(
        UserProfile, null=True, related_name='shop_assistant',
        on_delete=models.SET_NULL
    )
