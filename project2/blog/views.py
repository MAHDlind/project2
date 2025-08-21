from django.shortcuts import render, get_object_or_404
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from taggit.models import Tag


def blog_home(request, cat=None, tag=None):
    posts = models.Post.objects.filter(published_status=True)
    last_posts = posts.order_by("-published_date")[:3]

    filte = request.GET.get('q')
    if filte:
        posts = posts.filter(context__icontains=filte)

    if cat:
        posts = posts.filter(category__name=cat)

    if tag:
        posts = posts.filter(tags__name=tag)


    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    categories = models.Category.objects.all()
    all_tags = Tag.objects.all()

    content = {
        'posts': page_obj,
        'last_posts': last_posts,
        'categories': categories,
        'search_query': filte,
        'current_category': cat,
        'current_tag': tag,
        'all_tags': all_tags,
    }
    return render(request, 'blog/blog.html', content)


def blog_details(request, pid):
    post = get_object_or_404(models.Post, id=pid, published_status=True)
    author_profile = get_object_or_404(models.Profile, user=post.author.id)
    context = {'post': post, 'author': author_profile}
    return render(request, 'blog/blog-details.html', context)

