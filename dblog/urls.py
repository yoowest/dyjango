from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^about/$', views.about),
    url(r'^$', views.homepage),
    url(r'^quotes/', include('articles.urls')),

]

urlpatterns += staticfiles_urlpatterns()
static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
