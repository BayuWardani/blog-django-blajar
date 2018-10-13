# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Kategori(models.Model):
	nama = models.CharField(max_length=255)
	keterangan = models.TextField(blank=True,null=True)


	def __unicode__(self):
		return self.nama


	class Meta:
		verbose_name = 'Kategori'
		verbose_name_plural = 'Kategori'


class Tag(models.Model):
	nama = models.CharField(max_length=255)
	keterangan = models.TextField(blank=True,null=True)


	def __unicode__(self):
		return self.nama


	class Meta:
		verbose_name = 'Tag'
		verbose_name_plural = 'Tag'


