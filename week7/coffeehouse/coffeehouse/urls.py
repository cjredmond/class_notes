
from django.conf.urls import url
from django.contrib import admin
from menu_api.views import SpecialListAPIView, SpecialDetailAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^specials/$', SpecialListAPIView.as_view(), name = "special_list_api_view"),
    url(r'^specials/(?P<pk>\d+)/$', SpecialDetailAPIView.as_view(), name = "special_detail_api_view"),
]
