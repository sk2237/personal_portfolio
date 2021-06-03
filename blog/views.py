from django.shortcuts import render, get_object_or_404
from .models import blog_detail
# Create your views here.
def all_blogs(request):
  blogs = blog_detail.objects.all()
  return render(request, 'blogs/all_blogs.html',{'blogs':blogs})

def detail(request, blog_id):
  blog = get_object_or_404(blog_detail, pk=blog_id)
  return render(request, 'blogs/detail.html',{'blog':blog})
