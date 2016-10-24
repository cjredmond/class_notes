from django.conf.urls import url, include
from django.contrib import admin
from menu.views import IndexView, ProfileUpdateView, SpecialUpdateView, SpecialDeleteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^accounts/profile/$', ProfileUpdateView.as_view(), name="profile_view"),
    url(r'^special/(?P<pk>\d+)/update/$', SpecialUpdateView.as_view(), name="special_update_view"),
    url(r'^special/(?P<pk>\d+)/delete/$', SpecialDeleteView.as_view(), name="special_delete_view"),

]
