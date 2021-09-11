from django.contrib import admin
from django.conf.urls import url, include
from django.urls import path
from django.views.generic import TemplateView
from greensource_pages import urls as pages_url
from news import urls as news_url
from contact_us import urls as contact_url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps.views import sitemap
from greensource_pages.sitemaps import StaticSitemap
from contact_us.sitemaps import Static_Sitemap
from news.sitemaps import PostSitemap


sitemaps = {
    'static': StaticSitemap(),
    'news': PostSitemap,
    'contact_us': Static_Sitemap(),
}


urlpatterns = [
    path('greensource-webenergy/', admin.site.urls),
    url(r'^', include(pages_url)),
    url(r'^news/', include(news_url)),
    url(r'^', include(contact_url)),
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
    url(r'^robots\.txt$', TemplateView.as_view(template_name="Greensource-energy/robots.txt", content_type='text/plain')),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Greensource Energy Administration'
admin.site.site_title = 'Greensource Energy Consult'
admin.site.index_title = 'Greensource Energy Administration'
