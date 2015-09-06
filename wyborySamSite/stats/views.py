# coding=UTF-8
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from forms import UploadFileForm
from models import Election, Candidate
from properties_decoder import coder, decoder
import json


def create_models(request):
    json_file = json.load(request.FILES['file'])
    type = request.POST['options']

    for obj in json_file:
        new_model = {'type': type}
        for k, v in obj.iteritems():
            if 'Pkt' in k:
                try:
                    new_model['notes'].append({k: v})
                except:
                    new_model['notes'] = [{k: v}]
                continue
            k_coded = coder[k.encode('utf-8')]
            if 'kw' in k_coded or 'prez' in k_coded:
                try:
                    new_model['votes'].append({k_coded: v})
                except:
                    new_model['votes'] = [{k_coded: v}]
            else:
                new_model[coder[k.encode('utf-8')]] = v
        try:
            new_model['votes'] = json.dumps(new_model['votes'])
        except:
            pass
        try:
            new_model['notes'] = json.dumps(new_model['notes'])
        except:
            pass
        if type != 'candidate':
            model = Election(new_model)
        elif type != 'candidate':
            model = Candidate(new_model)
        model.save()


@login_required(login_url='/admin/login/')
def import_jsons(request):
    if request.method == 'GET':
        return render(request, 'importJsons.html', {'forms': UploadFileForm})
    elif request.method == 'POST':
        create_models(request)
        return render(request, 'importJsons.html', {'msg': 'OK'})
