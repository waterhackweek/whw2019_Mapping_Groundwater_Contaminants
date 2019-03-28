from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from tethys_sdk.gizmos import Button

@login_required()
def home(request):


    context = {}

    return render(request, 'gw_contaminants/home.html', context)