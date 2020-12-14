from django.shortcuts import render, get_object_or_404, redirect
from .models import Post,Category
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator, InvalidPage
from .forms import CommentForm


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
    post = get_object_or_404(Post,slug=slug)
    comments = post.comments.filter().order_by('-date')[:3]
    count = post.comments.count()
    new_comment = None
    if request.method == 'POST':
        comment_form = CommentForm(request.POST or None)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit = False)
            new_comment.post = post
            new_comment.save()
            return redirect("article_detail",slug = slug)
    else:
        comment_form = CommentForm()
    context = {
        'post':post, 
        'comments':comments, 
        'new_comment':new_comment, 
        'comment_form':comment_form,
        'count':count
    }
    return render(request,'article_detail.html', context)