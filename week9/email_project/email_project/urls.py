
from django.conf.urls import url
from django.contrib import admin
from app.views import IndexView, SendEmailView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', IndexView.as_view(), name="index_view"),
    url(r'^send_email/$', SendEmailView.as_view(), name="send_email_view")
]
