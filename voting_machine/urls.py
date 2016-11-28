
# voting_machine/urls.py

from django.conf.urls import url
from django.contrib import admin
import voting.views                         # XXX

urlpatterns = [
    url(r'^$', voting.views.index),         # XXX
    url(r'^date.*', voting.views.date),     # XXX
    url(r'^admin/', admin.site.urls),
]
