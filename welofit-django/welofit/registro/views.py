from django.shortcuts import render
from registro.forms import RegisterWizard
from django.http import HttpResponseRedirect
from models import *


def register_wizard(request):
    context = {}
    form = RegisterWizard()
    context['form'] = form
    return render(request, 'registro/base.html', context)


def register_data(request):
    context = {}

    if request.method == 'POST':

        form = RegisterWizard(request.POST)

        if form.is_valid():
            mc = form.cleaned_data
            print mc['name']
            user = UserData(name=mc['name'])
            user.save()
        else:
            print form.errors

    return render(request, 'registro/registro.html', context)
