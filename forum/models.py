from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Blog(models.Model):
	"""用户的博客"""
	title = models.CharField(max_length = 200)
	text = models.TextField()
	data_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User,on_delete = models.CASCADE)

	def __str__(self):
		"""返回字符串表达"""
		return self.title


class Comment(models.Model):
	"""用户的评论"""
	blog = models.ForeignKey(Blog,on_delete = models.CASCADE)
	text = models.TextField()
	data_added = models.DateTimeField(auto_now_add = True)
	owner = models.ForeignKey(User,on_delete = models.CASCADE)

	class Meta:
		verbose_name_plural = 'comments'

	def __str__(self):
		if len(self.text) >= 10:
			return f"{self.text}..."
		elif len(self.text) < 10:
			return f"{self.text}"