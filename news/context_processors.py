from news.models import Post,Category
from django.core.paginator import EmptyPage, PageNotAnInteger,Paginator


def posts_requests(request):
    category = Category.objects.all()
    page_kwarg = 'page'
    paginate_by = 6
    posts = Post.objects.all().order_by('-date')
    top_post = posts[:4]
    paginator = Paginator(posts, paginate_by)
    page_number = request.GET.get(page_kwarg)

    try:
        page = paginator.page(page_number)
    except PageNotAnInteger:
        page = paginator.page(1)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)

    context = {'categories':category,
                'post_list':page,
                'is_paginated':page.has_other_pages,
                'posts':top_post
            }
    
    return context
