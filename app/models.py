from django.db import models
from __future__ import unicode_literals


KIND_CHOICES = (
    ('Python技术', 'Python技术'),
    ('2', '2'),
    ('3', '3')
)

class Moment(models.Model):
    content = models.CharField(max_length=300)
    user_name = models.CharField(max_length=20, default="匿名")
    kind = models.CharField(max_length=20, choices=KIND_CHOICES, default=KIND_CHOICES[0])

