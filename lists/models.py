from django.db import models


class List(models.Model):
    # list =
    pass


class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)


