from django.core.paginator import Paginator
from django.shortcuts import render

from .models import PostModel, PostCategoryModel


def get_posts(request):
    search_query = request.GET.get('search', '')

    # search by title or description
    if search_query:
        posts = (PostModel.objects.filter(
            title__icontains=search_query
        ).order_by('-created_at') | PostModel.objects.filter(
            description__icontains=search_query).order_by('-created_at'))
    else:
        posts = PostModel.objects.all().order_by('-created_at')

    recent_posts = PostModel.objects.order_by('-created_at')[:4]
    categories = PostCategoryModel.objects.all()

    # pagination configuration, showing 8 posts on one page
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'recent_posts': recent_posts, 'categories': categories,
               'page_obj': page_obj}

    return render(request, 'posts.html', context)


def get_post_detail(request, pk):
    post = PostModel.objects.get(id=pk)
    # get related by category posts except itself
    related_posts = PostModel.objects.filter(
        category=post.category
    ).exclude(id=post.pk).order_by('-created_at')
    context = {'post': post, 'related_posts': related_posts}

    return render(request, 'post-detail.html', context)


def get_category(request, pk):
    category = PostCategoryModel.objects.get(id=pk)
    posts = PostModel.objects.filter(category=category).order_by('-created_at')

    # pagination configuration, showing 8 filtered by category posts per page
    paginator = Paginator(posts, 8)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {'category': category, 'page_obj': page_obj}

    return render(request, 'categories.html', context)
