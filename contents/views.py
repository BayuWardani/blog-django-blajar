# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from contents.models import Artikel
from masters.models import Kategori,Tag

# Create your views here.
def HomePage(request):
	artikels = Artikel.objects.all()
	kategori = Kategori.objects.all()
	tag = Tag.objects.all()

	extra_context = {
		'artikels':artikels,
		'kategoris':kategori,
		'tags':tag,
		'title':'Blog Untuk Belajar Django'
	}
	return render(request,'homepage.html',extra_context)