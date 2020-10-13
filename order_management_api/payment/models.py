from django.db import models
from django.utils import timezone

from config.models import AbstractBigIntPkModel

from product.models import Order


class Payment(AbstractBigIntPkModel):
    class Meta(AbstractBigIntPkModel.Meta):
        db_table = 'payments'

    SUCCESSFUL = 1
    UNSUCCESSFUL = 2

    STATUS_CHOICES = (
        (SUCCESSFUL, 'Successful'),
        (UNSUCCESSFUL, 'Unsuccessful')
    )

    status = models.SmallIntegerField(
        choices=STATUS_CHOICES, null=False, db_index=True,
        default=0
    )
    cash = models.BooleanField(default=False)
    card = models.BooleanField(default=False)
    invoice_date_created = models.DateTimeField(default=timezone.now)
    # amount paid by the client
    amount = models.BigIntegerField(null=False)
    # change from the customer's amount
    change = models.BigIntegerField(null=False, default=0)
    order = models.ForeignKey(Order, null=False, on_delete=models.CASCADE)
