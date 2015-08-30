from django.conf.urls import url
from stats.views import import_jsons

urlpatterns = [
    url(r'^data/import/$', import_jsons, name='index'),
]
