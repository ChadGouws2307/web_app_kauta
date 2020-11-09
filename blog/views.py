import random

from django.shortcuts import render
from .models import Post, Comment
from .forms import CommentForm


def blog_index(request):
    posts = Post.objects.all().order_by('-created_on')
    context = {
        "posts": posts,
    }

    view = random.random()
    if view >= 0.5:
        return render(request, "blog_index_v2.html", context)
    else:
        return render(request, "blog_index_v2.html", context)


def blog_category(request, category):
    posts = Post.objects.filter(
        categories__name__contains=category
    ).order_by('-created_on')

    context = {
        "category": category,
        "posts": posts
    }

    view = random.random()
    if view >= 0.5:
        return render(request, "blog_category.html", context)
    else:
        return render(request, "blog_category.html", context)


def blog_detail(request, slug):
    post = Post.objects.get(slug=slug)

    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(
                author=form.cleaned_data["author"],
                body=form.cleaned_data["body"],
                post=post
            )
            comment.save()

    comments = Comment.objects.filter(post=post)

    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    view = random.random()
    if view >= 0.5:
        return render(request, "blog_detail.html", context)
    else:
        return render(request, "blog_detail.html", context)

