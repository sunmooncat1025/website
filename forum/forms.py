from django import forms

from .models import Blog,Comment

class Blogform(forms.ModelForm):
	class Meta:
		model = Blog
		fields = ['title','text']
		labels = {'text':'内容','title':'标题'}
		widgets = {'text':forms.Textarea(attrs = {'cols':150})}

class Commentform(forms.ModelForm):
	class Meta:
		model = Comment
		fields = ['text']
		labels = {'text':''}
		widgets = {'text':forms.Textarea(attrs = {'cols':70})}