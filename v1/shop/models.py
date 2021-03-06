import uuid

from django.db import models
from django.conf import settings


class ShopType(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Cusine(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=63)

    def __str__(self):
        return self.name


class Country(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    name = models.CharField(max_length=255)
    alpha_two_code = models.CharField(max_length=2, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Countries'

    def __str__(self):
        return self.name


class Shop(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    shop_type = models.ForeignKey(ShopType, on_delete=models.DO_NOTHING, blank=True, null=True)
    name = models.CharField(max_length=255)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class ShopBranch(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)

    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)
    region = models.CharField(max_length=255, blank=True, null=True)
    state = models.CharField(max_length=255, blank=True, null=True)
    postal_code = models.CharField(max_length=7)
    latitude = models.FloatField()
    longitude = models.FloatField()

    eta_rang = models.CharField(max_length=7, blank=True, null=True)

    description = models.TextField()
    opening_time = models.TimeField()
    closing_time = models.TimeField()
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural = 'Shop Branches'

    def __str__(self):
        return self.shop.name + ": " + self.city


# model to handle the relationship between a User and
# a particular branch for authorization
class UserBranch(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    PermissionChoices = [
        (0, 'Viewer'),      # viewer is the employee of the shopBranch. can view, manage all the orders
        (1, 'Moderator'),   # has CRU permission for catogery, items and has ^ permission
        (2, 'Editor'),      # has CRUD permission for catogery, items and has ^ permission
        (3, 'Admin')        # can edit branch, assign permission to other users and has ^ permission
    ]
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    permission = models.IntegerField(choices=PermissionChoices, default=0)
    branch = models.ForeignKey(ShopBranch, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email + ": " + str(self.permission)

    class Meta:
        unique_together = ['user', 'branch']
        verbose_name_plural = 'User Branches'
