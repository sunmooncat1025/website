from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required


#creat your views here

def index(request):
	"""主页"""
	return render(request,'index.html')

#论坛
def forums(request):
	"""论坛"""
	from forum.models import Blog
	blogs = Blog.objects.order_by('-data_added')
	context = {'Blogs':blogs}
	return render(request,'forum.html',context)

@login_required
def blog(request,blog_id):
	"""单独博客文章"""
	#博客部分
	from forum.models import Blog
	blog = Blog.objects.get(id = blog_id)
	title = blog.title
	text = blog.text
	comments = blog.comment_set.order_by('-data_added')


	#评论部分
	from forum.forms import Commentform
	if request.method != 'POST':
		#没有提交数据，给予新的表单
		form = Commentform()
	else:
		#POST提交了数据，进行数据处理
		form = Commentform(data = request.POST)
		if form.is_valid():
			new_Comment = form.save(commit = False)
			new_Comment.blog = blog
			new_Comment.owner = request.user
			form.save()
			return redirect('forum',blog_id = blog_id)


	context = {'blog':blog,'title':title,'text':text,'comments':comments,'form':form}
	return render(request,'blog.html',context)

@login_required
def new_blog(request):
	"""用以给用户提供窗口进行添加博客"""
	from forum.forms import Blogform
	if request.method != 'POST':
		#没有提交数据，给予新的表单
		form = Blogform()
	else:
		#POST提交了数据，进行数据处理
		form = Blogform(data = request.POST)
		if form.is_valid():
			new_blog = form.save(commit = False)
			new_blog.owner = request.user
			new_blog.save()
			return redirect('forum')

	#显示空表单或指出表单数据无效
	context = {'form':form}
	return render(request,'new_blog.html',context)

#资料
def topic(request):
	"""资料库"""
	from data.models import Topic
	topics = Topic.objects.order_by('data_added')
	num1 = topics[0]
	entrys1 = num1.entry_set.order_by('-data_added')
	num2 = topics[1]
	entrys2 = num2.entry_set.order_by('-data_added')
	num3 = topics[2]
	entrys3 = num3.entry_set.order_by('-data_added')
	context = {'num1':num1,'num2':num2,'num3':num3,
				'entrys1':entrys1,'entrys2':entrys2,'entrys3':entrys3}
	return render(request,'topic.html',context)

def entry(request,entry_id):
	"""条目"""
	from data.models import Entry
	entry = Entry.objects.get(id = entry_id)
	title = entry.title
	datas = entry.data_set.order_by('-data_added')
	context = {'title':title,'datas':datas}
	return render(request,'entry.html',context)

def data(request,data_id):
	"""数据库"""
	from data.models import Data
	data = Data.objects.get(id = data_id)
	title = data.title
	text = data.text
	context = {'title':title,'text':text}
	return render(request,'data.html',context)

#用户组
def register(request):
	"""注册新用户"""
	from django.contrib.auth import login
	from django.contrib.auth.forms import UserCreationForm
	if request.method !='POST':
		#显示空表单
		form = UserCreationForm()
	else:
		#处理表单
		form = UserCreationForm(data = request.POST)

		if form.is_valid():
			new_user = form.save()
			#让用户能自动登录，而后定向到主页。
			login(request,new_user)
			return redirect('index')

	#显示空表单或指出表单无效
	context = {'form':form}
	return render(request,'register.html',context)


#关于我们
def about(request):
	"""关于我们"""
	return render(request,'about.html')