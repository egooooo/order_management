from django.db import models
from django.contrib.auth.models import User

from config.models import AbstractCreateUpdateModel


class UserProfile(AbstractCreateUpdateModel):
    class Meta(AbstractCreateUpdateModel.Meta):
        db_table = 'user_profiles'

    # Connect (1-to-1) user to django's auth_user models (for auth)
    user = models.OneToOneField(
        User, unique=True, null=True, on_delete=models.SET_NULL
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(db_index=True, max_length=256, unique=True)

    def __str__(self):
        return '{} ({} {})'.format(self.email, self.first_name, self.last_name)
