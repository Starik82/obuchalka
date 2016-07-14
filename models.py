# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User 
from django.utils import timezone
from django.contrib import auth
from django.conf import settings 


# Create your models here.
class Article(models.Model):
	class Meta():
		db_table = 'article'				
	article_title = models.CharField(max_length = 200)
	article_text = models.TextField()
	article_date = models.DateTimeField()
	article_likes = models.IntegerField(default=0)

class Comments(models.Model):
	class Meta():
		db_table = 'comments'
	comments_text = models.TextField(verbose_name="Comment")
	comments_article = models.ForeignKey(Article)
	comments_from = models.ForeignKey(User)
	comments_date = models.DateTimeField(default=timezone.now)
