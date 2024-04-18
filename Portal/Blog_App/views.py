from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render, HttpResponseRedirect
from django.urls import reverse
from django.views.generic.edit import CreateView, UpdateView, DeleteView 
from django.views.generic.list import ListView
from Blog_App import models
import uuid
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from Blog_App.forms import CommentForm


# Create your views here.

class IndexView(ListView):    
    model = models.Blog
    template_name = 'Blog_App/index.html'
    context_object_name = 'posts'


class Post(LoginRequiredMixin, CreateView):
    model = models.Blog
    fields = ['title','image','content']
    template_name = 'Blog_App/post.html'

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.author = self.request.user
        form_obj.slug = form_obj.title.replace(' ','-') + str(uuid.uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse('index'))
    

@login_required
def user_posts(request):
    id= request.user.id
    posts = models.Blog.objects.filter(author=id)
    dictionary={
        'posts': posts,
    }
    return render(request, 'Blog_App/user_posts.html', context=dictionary)


def post_details(request,slug):
    blog = models.Blog.objects.get(slug=slug)
    form = CommentForm()
    liked = models.Likes.objects.filter(author=request.user.id, blog=blog).exists()

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = blog
            comment.author = request.user
            comment.save()
            return HttpResponseRedirect(reverse('Blog_App:post_details', args=[slug]))
    dictionary = {
        'blog': blog,
        'form': form,
        'liked': liked,
    }
    return render(request, 'Blog_App/post_details.html', context=dictionary)


@login_required
def user_post_details(request, slug):
    blog = models.Blog.objects.get(slug=slug)
    dictionary = {
        'blog': blog,
    }
    return render(request, 'Blog_App/user_post_details.html', context=dictionary)


class UpdatePost(LoginRequiredMixin, UpdateView):
    model = models.Blog
    fields = ['title','image','content']
    template_name = 'Blog_App/update_post.html'

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.slug = form_obj.title.replace(' ','-') + str(uuid.uuid4())
        form_obj.save()
        return HttpResponseRedirect(reverse('Blog_App:user_posts'))
    


class PostDeleteView(LoginRequiredMixin, DeleteView):
    model = models.Blog
    template_name = 'Blog_App/delete_post.html'
    success_url = '/blog/user_posts/'



@login_required
def like(request, pk):
    blog =  models.Blog.objects.get(pk=pk)
    user = request.user
    liked = models.Likes.objects.filter(author = user, blog = blog).exists()

    if not liked:
        liked = models.Likes(author=user, blog = blog)
        liked.save()
    return HttpResponseRedirect(reverse('Blog_App:post_details', args=[blog.slug]))
    

@login_required
def undo_like(request, pk):
    blog =  models.Blog.objects.get(pk=pk)
    user = request.user
    liked = models.Likes.objects.filter(author = user, blog = blog).exists()
    
    if liked:
        liked = models.Likes.objects.filter(author=user, blog=blog)
        liked.delete()
    return HttpResponseRedirect(reverse('Blog_App:post_details', args=[blog.slug]))



class EditComment(LoginRequiredMixin, UpdateView):
    model = models.Comments
    fields = ['comment']
    template_name = 'Blog_App/edit_comment.html'
    success_url = '/blog/post_details/'

    def form_valid(self, form):
        form_obj = form.save(commit=False)
        form_obj.author = self.request.user
        form_obj.save()
        return HttpResponseRedirect(reverse('Blog_App:post_details', args=[form_obj.blog.slug]))



@login_required
def delete_comment(request,pk):
    comment = models.Comments.objects.get(pk=pk)
    blog = comment.blog
    comment.delete()
    return HttpResponseRedirect(reverse('Blog_App:post_details', args=[blog.slug]))