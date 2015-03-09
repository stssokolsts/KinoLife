from django.db import models


class UserProfile(BaseOrderInfo):
    """ Расширение стандартного класса User для хранения дополнительных полей"""
    user = models.OneToOneField(User)
    favorites = models.ManyToManyField(Product, null=True)

    def __unicode__(self):
        return 'User Profile for: ' + self.user.username
# Create your models here.
