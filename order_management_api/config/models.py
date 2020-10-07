from django.db import models


class AbstractCreateUpdateModel(models.Model):
    """
        Abstract CRUD model
        Includes pk - (int auto increment), created datetome field
        (current time when record has created), updated (current time
        when record has updated)
    """
    class Meta:
        abstract = True
        ordering = ['pk']

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class AbstractBigIntPkModel(AbstractCreateUpdateModel):
    class Meta():
        abstract = True
        ordering = ['pk']

    id = models.AutoField(primary_key=True)
