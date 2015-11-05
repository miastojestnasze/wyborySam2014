from django.conf.urls import url
from stats.views import import_jsons, get_geography, get_areas_tree,\
    get_district_stats, get_circle_stats, get_circuit_stats,\
    get_political_party_candidates, get_circle_candidates

urlpatterns = [
    url(r'^data/import/$', import_jsons, name='index'),
    url(r'^api/stats/areas-tree/$', get_areas_tree, name='index'), # returns  json {''}
    url(r'^api/stats/geography/$', get_geography, name='index'),
    url(r'^api/stats/(?P<election_type>[a-z]+)/(?P<district_name>[\w|\W]+)/$',
        get_district_stats, name='index'), # return_districts_data
    url(r'^api/stats/(?P<election_type>[a-z]+)/(?P<district_name>[\w|\W]+)/(?P<circle>[1-9]+)/$',
        get_circle_stats, name='index'), # return_circle_data
    url(r'^api/stats/(?P<election_type>[a-z]+)/(?P<district_name>[\w|\W]+)/(?P<circle>[1-9]+)/(?P<circuit>[1-9]+)/$',
        get_circuit_stats, name='index'), #return_circuit_data
    url(r'^api/candidates/(?P<election_type>[a-z]+)/(?P<district_name>[\w|\W]+)/(?P<party>[\w|\W]+)/$', 
        get_political_party_candidates, name='index'),
    url(r'^api/candidates/(?P<election_type>[a-z]+)/(?P<district_name>[\w|\W]+)/(?P<circle>[1-9]+)/$', 
        get_circle_candidates, name='index'),
]
