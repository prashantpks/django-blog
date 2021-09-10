from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponseRedirect, redirect
from django.views.generic import CreateView, UpdateView, ListView, TemplateView, DetailView, DeleteView
from .models import Blog, Comment, Likes
from django.urls import reverse, reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
import uuid

from .forms import CommentForm



def home(request):
    latest_post = Blog.objects.order_by('-publish_date')[:6]
    data = {
        'latest_post':latest_post,
    }
    return render(request,'blog_post/home.html',data)

def mybloglist(request):
    blogs = Blog.objects.order_by('-update_date')

    data = {
        'blogs':blogs,
    }
    return render(request,'blog_post/my_blog_list.html',data)



class CreateBlog(CreateView,LoginRequiredMixin):
    model = Blog
    template_name = 'blog_post/create_blog.html'
    fields = ('blog_title','blog_content','blog_image',)

    def form_valid(self,form):
        blog_obj = form.save(commit = False)
        blog_obj.author = self.request.user
        # Creating slug
        title = blog_obj.blog_title
        blog_obj.slug = title.replace(' ','-')+'-'+ str(uuid.uuid4())
        form.save()
        return HttpResponseRedirect(reverse('my_blog_list'))


def blog_detail(request,slug):
    blog = Blog.objects.get(slug = slug)
    
    comment_data = Comment.objects.filter(blog = blog)
    latest_post = Blog.objects.order_by('-publish_date')[:6]

    if request.method == 'POST':
        user = request.user
        blog = blog
        comment = request.POST['comment']
        comment_obj = Comment(user = user,blog = blog, comment = comment)
        comment_obj.save()
        return HttpResponseRedirect(reverse('blog_detail',kwargs={'slug':slug}))
    


    data = {
        'blog':blog,
        'comment_data': comment_data, 
        'latest_post': latest_post,  
    }
    return render(request,'blog_post/blog_detail.html',data)


class MyBlog(LoginRequiredMixin,TemplateView):
    template_name = 'blog_post/my_blog.html'


class UpdateBlog(LoginRequiredMixin,UpdateView):
    model = Blog
    fields = ('blog_title','blog_content','blog_image',)
    template_name = 'blog_post/edit_blog.html'

    # Redirect after updating
    def get_success_url(self,**kwargs):
        return  reverse_lazy('blog_detail',kwargs = {'slug': self.object.slug})
