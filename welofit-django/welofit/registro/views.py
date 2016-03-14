from django.shortcuts import render

from registro.forms import register_wizard_form

from django.http import HttpResponseRedirect

def register_wizard(request):
    context = {}
    form = register_wizard_form()    
    context['form'] = form
    return render(request, 'registro/base.html', context)

def register_data(request):
    context = {}

    if request.method == 'POST':

        form = register_wizard_form(request.POST)
        
        if form.is_valid():
            mc = form.cleaned_data
            print mc
        else:
            print "no valido"

    return render(request, 'registro/registro.html', context)