
from django.conf.urls import url
from django.contrib import admin

from app.views import index_view, favorites_view

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index_view, name="index_view"),
    url(r'^favorites/$', favorites_view, name="favorites_view")
]
