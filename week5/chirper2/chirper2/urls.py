from django.conf.urls import url, include
from django.contrib import admin
from app.views import about_view, ChirpView, ChirpDetailView, \
                      ChirpCreateView, ChirpUpdateView, UserCreateView, \
                      ChirpVoteView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^$', ChirpView.as_view(), name="chirp_view"),
    url(r'^chirps/create$', ChirpCreateView.as_view(), name="chirp_create_view"),
    url(r'^chirps/(?P<pk>\d+)/$', ChirpDetailView.as_view(), name="chirp_detail_view"),
    url(r'^chirps/(?P<pk>\d+)/update/$', ChirpUpdateView.as_view(), name="chirp_update_view"),
    url(r'^about/$', about_view, name="about_view"),
    url(r'^create_user/$', UserCreateView.as_view(), name="user_create_view"),
    url(r'^chirps/(?P<pk>\d+)/upvote$', ChirpVoteView.as_view(), name="chirp_upvote_view"),
    url(r'^chirps/(?P<pk>\d+)/downvote$', ChirpVoteView.as_view(), name="chirp_downvote_view"),

]
