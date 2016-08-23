from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.contrib.contenttypes.fields import ContentType
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Post, Category, Tag
from .forms import PostForm
from comments.models import Comment

# Create your views here.


def post_list(request):
    posts_list = Post.objects.all()
    query = request.GET.get('q')
    if query:
        posts_list = Post.objects.filter(
            Q(title__icontains=query) | Q(content__icontains=query) |
            Q(user__first_name__icontains=query) | Q(user__last_name__icontains=query)
        ).distinct()
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


@login_required
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


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    content_type = ContentType.objects.get_for_model(Post)
    comments = Comment.objects.filter(content_type=content_type, object_id=post.id)
    context = {
        'post': post,
        'comments': comments
    }
    return render(request, 'post-detail.html', context)


def post_update(request, slug):
    post = get_object_or_404(Post, slug=slug)
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


def post_delete(request, slug):
    post = get_object_or_404(Post, slug=slug)
    post.delete()
    messages.success(request, "Successfully Deleted")
    return redirect('post-list')


def post_category(request, slug):
    cat_name = get_object_or_404(Category, slug=slug)
    cat_list = Post.objects.filter(categories__slug=slug)
    paginator = Paginator(cat_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'cat_name': cat_name
    }
    return render(request, 'post-category.html', context)


def post_tags(request, slug):
    tag_name = get_object_or_404(Tag, slug=slug)
    tag_list = Post.objects.filter(tags__slug=slug)
    paginator = Paginator(tag_list, 4)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    context = {
        'posts': posts,
        'tag_name': tag_name
    }
    return render(request, 'post-tag.html', context)


