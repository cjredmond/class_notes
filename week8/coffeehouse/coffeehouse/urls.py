
from django.conf.urls import url
from django.contrib import admin
from menu.views import SpecialListView, SpecialCreateView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', SpecialListView.as_view(), name="special_list_view"),
    url(r'^create/$', SpecialCreateView.as_view(), name="special_create_view")
]
