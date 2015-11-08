# coding=UTF-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import JsonResponse
from forms import UploadFileForm
from models import Election, Candidate, Vote
from properties_decoder import coder, decoder
from tree import get_election_tree
import json


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


def get_areas_tree(request):
    tree = {}
    for el in Election.objects.filter().distinct('election_type'):
        if not el.election_type in ['president_first_turn_districts', 'president_second_turn_districts', 'voivodeship']:
            tree[el.election_type] = get_election_tree(el.election_type)

    return JsonResponse(tree)

def get_district_stats(request, election_type, district_name):
    print election_type, district_name
    pass


def get_circle_stats(request, election_type, district_name, circle):
    print election_type, district_name, circle
    pass


def get_circuit_stats(request, election_type, district_name, circle, circuit):
    print election_type, district_name, circle, circuit
    pass


def get_political_party_candidates(request, election_type, district_name, party):
    pass


def get_circle_candidates(request, election_type, district_name, circle):
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
