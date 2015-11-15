from django.conf.urls import url
from stats.views import import_jsons, get_geography, get_areas_tree,\
    get_stats, get_candidates

urlpatterns = [
    # url(r'^data/import/$', import_jsons, name='data-import'),
    url(r'^api/stats/areas-tree/$', get_areas_tree, name='areas-tree'), # returns  json {''}
    url(r'^api/stats/geography/$', get_geography, name='geography'),
    url(r'^api/stats/(?P<election_type>.+)/district-(?P<district>[\w|\W]+)/circle-(?P<number_of_district>[0-9]+)/circuit-(?P<number_of_electoral_circuit>[0-9]+)/$',
        get_stats, name='electoral-circuit-stats'),
    url(r'^api/stats/(?P<election_type>.+)/district-(?P<district>[\w|\W]+)/circuit-(?P<number_of_electoral_circuit>[0-9]+)/$',
        get_stats, name='district-stats'),
    url(r'^api/stats/(?P<election_type>.+)/district-(?P<district>[\w|\W]+)/circle-(?P<number_of_district>[0-9]+)/$',
        get_stats, name='electoral-circle-stats'),
    url(r'^api/stats/(?P<election_type>.+)/circle-(?P<number_of_district>[0-9]+)/$',
        get_stats, name='district-stats'), 
    url(r'^api/stats/(?P<election_type>.+)/circle-(?P<number_of_district>[0-9]+)/circuit-(?P<number_of_electoral_circuit>[0-9]+)/$',
        get_stats, name='district-stats'),
    url(r'^api/stats/(?P<election_type>.+)/district-(?P<district>[\w|\W]+)/$',
        get_stats, name='district-stats'),
    url(r'^api/stats/(?P<election_type>.+)/$', get_stats, name='stats'),
    url(r'^api/candidates/(?P<election_type>[a-z]+)/district-(?P<district>[\w|\W]+)/pparty-(?P<election_committee>[\w|\W]+)/$', 
        get_candidates, name='candidates'),
    url(r'^api/candidates/(?P<election_type>[a-z]+)/district-(?P<district>[\w|\W]+)/circle-(?P<number_of_district>[0-9]+)/$', 
        get_candidates, name='index'),
    url(r'^api/candidates/(?P<election_type>[a-z]+)/district-(?P<district>[\w|\W]+)/circle-(?P<number_of_district>[0-9]+)/circuit-(?P<number_of_electoral_circuit>[0-9]+)/$', 
        get_candidates, name='index'),
]
