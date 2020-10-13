from django.db import models
from django.contrib.auth.models import User

from config.models import AbstractCreateUpdateModel


class UserRole(AbstractCreateUpdateModel):
    class Meta(AbstractCreateUpdateModel.Meta):
        db_table = 'user_roles'

    SHOP_ASSISTANT_SLUG = 'shop_assistant'
    CASHIER_SLUG = 'cashier'
    ACCOUNTANT_SLUG = 'accountant'

    name = models.CharField(max_length=32, db_index=True)
    slug = models.CharField(max_length=32, unique=True)
    is_admin = models.BooleanField(db_index=True, default=False)


class UserProfile(AbstractCreateUpdateModel):
    class Meta(AbstractCreateUpdateModel.Meta):
        db_table = 'user_profiles'

    first_name = models.CharField(max_length=31)
    last_name = models.CharField(max_length=31)
    email = models.EmailField(db_index=True, unique=True, max_length=32)
    role = models.ForeignKey(UserRole, null=False, on_delete=models.CASCADE)
    # Connect (1-to-1) user to django's auth_user models (for auth)
    user = models.OneToOneField(
        User, unique=True, null=True, on_delete=models.SET_NULL
    )

    def is_shop_assistant(self):
        return self.role.slug == UserRole.SHOP_ASSISTANT_SLUG

    def is_cashier(self):
        if self.role.slug == UserRole.CASHIER_SLUG:
            return True
        return False

    def is_accountant(self):
        if self.role.slug == UserRole.ACCOUNTANT_SLUG:
            return True
        return False

    def __str__(self):
        return f'{self.email} ({self.first_name} {self.last_name})'
