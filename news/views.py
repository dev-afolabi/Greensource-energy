from django.shortcuts import render
from .models import Post,Category
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator, InvalidPage


#Create your views here.
def article_category(request,category_name_slug):
    page_kwarg = 'page'
    paginate_by = 6
    category = Category.objects.get(slug=category_name_slug)
    cat_posts = Post.objects.filter(category=category)
    paginator = Paginator(cat_posts, paginate_by)
    page_number = request.GET.get(page_kwarg)
    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    return render(request, 'article_category.html', {'cat_posts':cat_posts,'is_paginated':page.has_other_pages})


def article_list(request):
    return render(request,'article_list.html')


def article_detail(request,slug):
    post = Post.objects.get(slug=slug)
    return render(request, 'article_detail.html',{'post':post})


