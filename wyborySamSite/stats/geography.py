from models import Election
from django.db.models import Sum


def create_geo_data(**kwargs):
    #Does I have to sum Sum('number_of_proxies') and Sum('number_of_voters')?
    # 'cards_valid' -> glosow oddanych
    data = Election.objects.filter(**kwargs).aggregate(Sum('number_of_voters'), Sum('votes_valid'), Sum('cards_given'), Sum('cards_valid'), Sum('votes_invalid'))
    for k, v in data.iteritems():
        data[k.split('__')[0]] = data.pop(k)

    data['votes_valid_p'] = round(float(data['votes_valid'])/float(data['cards_valid'])*100, 2)
    data['attendance_p'] = round(float(data['cards_valid'])/float(data['number_of_voters'])*100, 2)
    return data
