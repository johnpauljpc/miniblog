from django.shortcuts import render
from blog.models import Post

# Create your views here.

def home(request):

	posts = Post.objects.filter(status=Post.ACTIVE)
	return render(request, 'home.html', {'posts':posts})


def about(request):
	return render(request, 'about.html')


def robots_txt(request):
    text = [
        "User-Agent: *",
        "Disallow: /admin/",
    ]
    return HttpResponse("\n".join(text), content_type="text/plain")