from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from .models import Post
from .forms import PostForm

# Create your views here.


def post_list(request):
    posts_list = Post.objects.all().order_by("-timestamp")
    paginator = Paginator(posts_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    context = {
        'posts': posts
    }
    return render(request, "post-list.html", context)


def post_create(request):
    form = PostForm(request.POST, request.FILES)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Created")
        return redirect('post-list')
    context = {
        "form": form
    }
    return render(request, 'post-form.html', context)


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    context = {
        'post': post
    }
    return render(request, 'post-detail.html', context)


def post_update(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = PostForm(request.POST, request.FILES, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Successfully Saved")
        return redirect('post-list')
    context = {
        'post': post,
        'form': form
    }
    return render(request, 'post-form.html', context)


def post_delete(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('post-list')
