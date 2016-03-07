from django.shortcuts import render

from registro.forms import user_data_form, fitness_data_form, body_data_form

def register_wizard(request):
    context = {}
    form_user = user_data_form()    
    context['form_user'] = form_user
    form_fitness = fitness_data_form()    
    context['form_fitness'] = form_fitness
    form_body = body_data_form()
    context['form_body'] = form_body
    return render(request, 'base.html', context)
