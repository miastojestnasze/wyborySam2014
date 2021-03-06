# coding=UTF-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.db.models import Sum
from django.forms.models import model_to_dict
from django.http import JsonResponse
from forms import UploadFileForm
from models import Election, Candidate, Vote
from properties_decoder import coder, coder_election_types
from tree import get_election_tree
from geography import create_geo_data
import json

tree = []
cashed_stats = {}
# Vote.objects.filter(election__election_type='district').distinct('political_party') and list all political parties

# Vote.objects.filter(
#     election__election_type='district', 
#     political_party='Komitet Wyborczy Wyborców Miasto Jest Nasze-Mieszkańców Śródmieścia')
# .aggregate(Sum('amount'))
# >{'amount__sum': 5581}


#//Sample query with sum of votes, statictics
# Election.objects.filter(election_type='district')
#.aggregate(Sum('number_of_voters'), Sum('votes_valid'), Sum('cards_given'), Sum('cards_taken'))

def get_geography(request):
    pass


# TODO: move body to tree.py and create new function
def get_areas_tree(request):
    if len(tree) == 0:
        for el in Election.objects.filter().distinct('election_type'):
            if not el.election_type in ['president_first_turn_districts', 'president_second_turn_districts']:
                election = {
                    'name': coder_election_types[el.election_type],
                    'children': get_election_tree(el.election_type),
                    'url': 'stats/' + el.election_type + '/',
                    'type': el.election_type
                }
                tree.append(election)

    return JsonResponse(tree, safe=False)


def get_stats(request, **kwargs):
    votes_kwargs = {}
    keys = ['district', 'number_of_electoral_circuit', 'number_of_district']    

    district_data = {'geography': create_geo_data(**kwargs), 'votes': []}
    el_type = kwargs['election_type'];
    
    if 1 == len(kwargs.keys()) and not kwargs.keys()[0] in keys and el_type in cashed_stats:
        return JsonResponse(cashed_stats[el_type])

    for k, v in kwargs.iteritems():
        if k != 'political_party':
            votes_kwargs['election__' + k] = float(v) if 'number' in k else v

    for v in Vote.objects.filter(**votes_kwargs).distinct('political_party'):
        votes_kwargs['political_party'] = v.political_party
        obj = {
            'political_party': v.political_party,
            'amount': Vote.objects.filter(**votes_kwargs).aggregate(Sum('amount'))['amount__sum']
        }
        votes_kwargs.pop('political_party')
        obj['percentage'] = round(float(obj['amount'])/ Vote.objects.filter(**votes_kwargs).aggregate(Sum('amount'))['amount__sum']*100, 2)
        district_data['votes'].append(obj)

    if kwargs['election_type'] in ['district', 'city_council', 'voivodeship']:
        district_data['candidates'] = get_candidates(**kwargs)

    if 1 == len(kwargs.keys()) and not kwargs.keys()[0] in keys and not el_type in cashed_stats:
        cashed_stats[el_type] = district_data

    return JsonResponse(district_data)


def get_candidates(**kwargs):
    if kwargs['election_type'] == 'district':
        kwargs['grade'] = 'DZ'
    elif kwargs['election_type'] == 'city_council':
        kwargs['grade'] = 'GM'
    elif kwargs['election_type'] == 'voivodeship':
        kwargs['grade'] = 'WO'
    try:
        kwargs['district']
        kwargs['voivodeship'] = kwargs.pop('district')
        if kwargs['election_type'] == 'voivodeship':
            kwargs.pop('voivodeship')
    except:
        pass
    try:
        kwargs.pop('number_of_electoral_circuit')
    except:
        pass
    kwargs.pop('election_type')
    candidates = []

    for c in Candidate.objects.filter(**kwargs):
        canditate = model_to_dict(c)
        canditate['fullName'] = canditate['names'].split(" ")[0] + ' ' + canditate['surname']
        candidates.append(canditate)
    return candidates


def get_candidates_view(request, **kwargs):
    pass


def create_models(request):
    json_file = json.load(request.FILES['file'])
    type = request.POST['options']

    for obj in json_file:
        new_model = {'election_type': type}
        votes = []
        for k, v in obj.iteritems():
            if 'Pkt' in k:
                try:
                    new_model['notes'].append({k: v})
                except:
                    new_model['notes'] = [{k: v}]
                continue
            
            k_coded = coder[k.encode('utf-8')]

            if 'kw' in k_coded or 'prez' in k_coded:
                vote = Vote(political_party=k, amount=v)
                vote.save()
                votes.append(vote)
            else:
                if 'Gmina' == k:
                    new_model['district'] = v
                else:
                    new_model[coder[k.encode('utf-8')]] = v
        try:
            new_model['notes'] = json.dumps(new_model['notes'])
        except:
            pass
        if type != 'candidate':
            election_model = Election(**new_model)
            election_model.save()
        elif type == 'candidate':
            election_model = Candidate(**new_model)
            election_model.save()
            continue

        for v in votes:
            v.election = election_model
            v.save()


@login_required(login_url='/admin/login/')
def import_jsons(request):
    if request.method == 'GET':
        return render(request, 'importJsons.html', {'forms': UploadFileForm})
    elif request.method == 'POST':
        create_models(request)
        return render(request, 'importJsons.html', {'msg': 'OK'})
