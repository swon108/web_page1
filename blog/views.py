from django.views.generic import ListView, DetailView
from .models import Post
from django.shortcuts import render
# Create your views here.

class PostList(ListView):
    model = Post
    template_name = 'blog/index.html'
    ordering = '-pk'

class PostDetail(DetailView):
    model = Post


    #template_name = 'blog/post_list.html'

#def index(request) :
#    posts = Post.objects.all()

#    return render(
#        request,
#    'blog/post_list.html',
#    {
#        'posts' : posts,
#    }
#)

#def single_post_page(request,pk) :
#    post = Post.objects.get(pk=pk)

#    return render (
#        request,
#        'blog/single_post_page.html',
#    {
#        'post' :post,
#    }
#)