from __future__ import unicode_literals
from django.utils.translation import ugettext, ugettext_lazy as _

from django.db import models

class Post(models.Model):

	title = models.CharField((_('Title')), max_length=100)	
	content = models.TextField((_('Content')))
	date = models.DateTimeField(auto_now_add=True, blank=True)

	def __str__(self):
		return self.title

	