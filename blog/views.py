from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Q
from .models import Post, Comment, Category
from .forms import CommentForm
from django.views.generic import CreateView
# Create your views here.
def detail(request,category_slug, slug, status=Post.ACTIVE):
	post=get_object_or_404(Post, slug=slug)
	
	if request.method== 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment= form.save(commit=False)
			comment.post=post
			comment.save()

			return redirect('detail', slug=slug)
	form = CommentForm()

	comments= Comment.objects.all()
	category= Category.objects.all()
		

	conttext={'posts':post, 'form':form, 'comments':comments, 'category':category}
	return render(request, 'detail.html', conttext)

def category(request, slug):
	category = get_object_or_404(Category, slug=slug)
	posts=category.posts.filter(status=Post.ACTIVE)

	

	return render(request, 'category.html', {'category':category, 'posts':posts})

def search(request):
	query = request.GET.get('query', '')
	posts = Post.objects.filter(status=Post.ACTIVE).filter(Q(title__icontains=query)|Q(body__icontains=query)|Q(intro__icontains=query))	
	return render(request, 'search.html', {'query':query, 'posts':posts})
