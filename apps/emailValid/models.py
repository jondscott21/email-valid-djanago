from __future__ import unicode_literals
from django.contrib import messages
from django.db import models
import re
EMAIL_REGEX = re.compile(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)")
# Create your models here.
class Emanager(models.Manager):
    def reg(self, email):
        if EMAIL_REGEX.match(email):
            return super(Emanager, self).create(email=email)
        else:
            return False
class Email(models.Model):
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    objects = Emanager()

