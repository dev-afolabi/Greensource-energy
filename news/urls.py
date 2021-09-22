from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.article_list, name='article_list'),
    url(r'^(?P<slug>[\w-]+)/$', views.article_detail, name='article_detail'),
    url(r'^category/(?P<slug>[\w-]+)/$', views.article_detail, name='article_detail'),
    url(r'^category/(?P<category_name_slug>[\w\-]+)/$', views.article_category, name='article-category')
]