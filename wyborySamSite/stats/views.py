from django.contrib.auth.decorators import login_required
from django.shortcuts import render
# Create your views here.


@login_required(login_url='/admin/login/')
def import_jsons(request):
    return render(request, 'importJsons.html')
