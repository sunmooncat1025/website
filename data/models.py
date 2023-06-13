from django.db import models

# Create your models here.

class Topic(models.Model):
	"""资料的主题"""
	title = models.CharField(max_length = 200)
	data_added = models.DateTimeField(auto_now_add = True,null=True)

	def __str__(self):
		"""返回字符串表示"""
		return self.title

class Entry(models.Model):
	"""资料的具体条目"""
	topic = models.ForeignKey(Topic,on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	data_added = models.DateTimeField(auto_now_add = True,null=True)

	def __str__(self):
		"""返回字符串表示"""
		return self.title

class Data(models.Model):
	"""资料的具体数据"""
	entry = models.ForeignKey(Entry,on_delete = models.CASCADE)
	title = models.CharField(max_length = 200)
	text = models.TextField()
	data_added = models.DateTimeField(auto_now_add = True,null=True)

	def __str__(self):
		"""返回字符串表示"""
		return self.title