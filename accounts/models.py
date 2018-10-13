# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class Account(AbstractUser):
	nomor_hp = models.CharField(max_length=12,blank=True,null=True)
	alamat = models.TextField(blank=True,null=True)


	def __unicode__(self):
		return self.username


	class Meta:
		verbose_name = 'Account'
		verbose_name_plural = 'Account'