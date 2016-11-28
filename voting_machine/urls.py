
# voting_machine/urls.py

from django.conf.urls import url
from django.contrib import admin
import voting.views                        

urlpatterns = [
    url(r'^$', voting.views.index),        
    url(r'^(?P<poll_id>\d+)/$', voting.views.one_poll),
    url(r'^admin/', admin.site.urls),
]
