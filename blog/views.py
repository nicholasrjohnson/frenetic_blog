from re import I, template
from time import time
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views import View 
from django.http import HttpResponseRedirect
from django.utils import timezone
from .forms import BrowseForm, AddEditPostForm
from django.db.models import Max
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth import authenticate, login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post

def index(request):
    return render(request, 'blog/index.html')

def browse(request, page):
    postsModel = Post.objects.get_queryset().order_by('-pub_date')
    paginator = Paginator(postsModel, 5) #get 5 posts per page

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    if(request.method == 'POST'):
        if 'viewPost' in request.POST:
            form = BrowseForm(request.POST, posts)
            if form.is_valid():
                if 'choice' in request.POST:
                    context = {}
                    context['form'] = form
                    context['page'] = page
                    context['posts'] = posts
                    print("Before slug")
                    slug = request.POST['choice']
                    print("After slug")
                    return HttpResponseRedirect(reverse('blog:viewpost', args=[slug]))
        elif 'addPost' in request.POST:
            return HttpResponseRedirect(reverse('blog:addpost'))
        elif 'editPost' in request.POST:
            form = BrowseForm(request.POST, posts)
            if form.is_valid():
                if 'choice' in request.POST:
                    context = {}
                    context['form'] = form
                    context['page'] = page
                    context['posts'] = posts
                    slug = request.POST['choice']
                    return HttpResponseRedirect(reverse('blog:editpost', args=[slug]))
        elif 'deletePost' in request.POST:
            form = BrowseForm(request.POST, posts)
            if form.is_valid():
                if 'choice' in request.POST:
                    context = {}
                    context['form'] = form
                    context['page'] = page
                    context['posts'] = posts
                    slug = request.POST['choice']
                    return HttpResponseRedirect(reverse('blog:deletepost', args=[slug]))

    form = BrowseForm(posts)
    context = {}
    context['form'] = form
    context['page'] = page
    context['posts'] = posts
    return render(request, 'blog/browse.html', context)
        
def viewpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context={}
    context['post'] = post
    context['slug'] = slug
    return render(request, 'blog/viewpost.html', context) 

@login_required(login_url='/accounts/login')
def addpost(request):
    if request.method == 'POST':
        form = AddEditPostForm(request.POST)
        if form.is_valid():
            if Post.objects.all():
                if Post.objects.count() > 50:
                    return HttpResponseRedirect(reverse('blog:toomanyposts'))
            post = Post(created_by=request.user) 
            post.title = form.cleaned_data['postTitle']
            post.body = form.cleaned_data['postText']
            post.pub_date = timezone.now()
            post.edited_date = timezone.now()
            post.save() 
            return HttpResponseRedirect(reverse('blog:postadded', args=[post.slug]))
    form = AddEditPostForm()
    context = {}
    context['form'] = form
    return render(request, 'blog/addpost.html', context)

@login_required(login_url='/accounts/login')
def editpost(request, slug):
    if request.method == 'POST':
        form = AddEditPostForm(request.POST)
        if form.is_valid():
            post=get_object_or_404(Post, slug=slug)
            post.title = form.cleaned_data['postTitle']
            post.body = form.cleaned_data['postText']
            post.edited_date=timezone.now()
            post.save()
            return HttpResponseRedirect(reverse('blog:postedited', args=[slug]))
    post=get_object_or_404(Post, slug=slug)
    data = {'postTitle': post.title, 'postText': post.body}
    form = AddEditPostForm(initial=data)
    context = {}
    context['form'] = form
    context['slug'] = slug
    return render(request, 'blog/editpost.html', context)

@login_required(login_url='/accounts/login')
def deletepost(request, slug):
    context = {}
    post = get_object_or_404(Post, slug=slug)
    context['slug'] = post.slug
    post.delete()
    return render(request, 'blog/postdeleted.html', context)

@login_required(login_url='/accounts/login')
def postadded(request, slug):
    context = {}
    context['slug'] = slug
    return render(request, 'blog/postadded.html', context)

@login_required(login_url='/accounts/login')
def toomanyposts(request):
    return render(request, 'blog/toomanyposts.html')

@login_required(login_url='/accounts/login')
def postdeleted(request, slug):
    context = {}
    context['slug'] = slug
    return render(request, 'blog/postdeleted.html', context)
    
@login_required(login_url='/accounts/login')
def postedited(request, slug):
    context = {}
    context['slug'] = slug
    return render(request, 'blog/postedited.html', context)