from django.shortcuts import render
from .models import blog_detail
# Create your views here.
def all_blogs(request):
  blogs = blog_detail.objects.all()
  return render(request, 'blogs/all_blogs.html',{'blogs':blogs})
