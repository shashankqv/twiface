from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Models):
    user = models.OneToOneField(User, verbose_name=_('user'),
            related_name='profile')

    @property
    def first_name(self):
        return self.user.first_name

    @property
    def last_name(self):
        return self.user.last_name

    @property
    def name(self):
        return (self.user.first_name + ' ' + self.user.last_name) or user.username
