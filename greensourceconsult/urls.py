from django.contrib import admin
from django.conf.urls import url,include
from django.urls import path
from greensource_pages import urls as pages_url
from news import urls as news_url
from contact_us import urls as contact_url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('greensource-webconsult/', admin.site.urls),
    url(r'^', include(pages_url)),
    url(r'^news/', include(news_url)),
    url(r'^', include(contact_url)),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

admin.site.site_header = 'Greensource Energy Administration'
admin.site.site_title = 'Greensource Energy Consult'
admin.site.index_title = 'Greensource Energy Administration'
