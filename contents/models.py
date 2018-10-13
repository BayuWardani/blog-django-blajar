# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from accounts.models import Account
from masters.models import Kategori,Tag

# Create your models here.
class Artikel(models.Model):
	judul = models.CharField(max_length=255)
	author = models.ForeignKey(Account)
	kategori = models.ForeignKey(Kategori)
	tag = models.ManyToManyField(Tag,blank=True,null=True)
	body = models.TextField()
	slug = models.SlugField(max_length=255,unique=True)
	cover = models.ImageField(upload_to='image/',blank=True,null=True)


	def __unicode__(self):
		return self.judul


	class Meta:
		verbose_name = 'Artikel'
		verbose_name_plural = 'Artikel'