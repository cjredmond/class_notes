
from django.conf.urls import url
from django.contrib import admin
from menu.views import SpecialListView, SpecialCreateView, SpecialUpdateView, SpecialAPIListView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/specials/$', SpecialAPIListView.as_view(), name="special_list_api_view"),
    url(r'^$', SpecialListView.as_view(), name="special_list_view"),
    url(r'^create/$', SpecialCreateView.as_view(), name="special_create_view"),
    url(r'^update/(?P<pk>\d+)/$', SpecialUpdateView.as_view(), name="special_update_view")
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
