from django.forms import ModelForm
from django import forms
from registro.models import UserData, FitnessData, BodyData
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Div, Fieldset, ButtonHolder, HTML, Submit 


class RegisterWizard(forms.Form):
    GENDER_CHOICES = (
        ('M', 'male'),
        ('F', 'female')
    )
    PLACE_CHOICES = (
        ('0', 'Gym'),
        ('1', 'Out'),
        ('2', 'Home')
    )
    
    EQUIP_CHOICES = (
        ('0', 'Dumbbell'),
        ('1', 'Bench')
    )
    CHAT_CHOICES = (
        ('0', '10:00 ~ 12:00'),
        ('1', '12:00 ~ 14:00'),
        ('2', '14:00 ~ 16:00'),
        ('3', '16:00 ~ 18:00'),
        ('4', '18:00 ~ 20:00'),
        ('5', '20:00 ~ 22:00'),
    )  
    BIO_CHOICES = (
        ('0', 'No'),
        ('1', 'Yes')
    )
    GOALS_CHOICES = (
        ('0', 'build muscle'),
        ('1', 'lose weight'),
        ('2', 'muscle tone')
    )
    ACTIVITY_CHOICES = (
        ('0', 'Office worker getting little or no exercise'),
        ('1', 'Construction worker or person running one hour daily'),
        ('2', 'Agricultural worker (non mechanized) or person swimming two hours daily'),
        ('3', 'Competitive cyclist')
    )
    name = forms.CharField()
    username = forms.CharField()
    email = forms.CharField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    birthdate = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control'}))
    genre = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    training_place = forms.ChoiceField(widget=forms.RadioSelect, choices=PLACE_CHOICES)
    equipment = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple, choices=EQUIP_CHOICES)
    chat_availability = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=CHAT_CHOICES)
    fitness_bio = forms.ChoiceField(widget=forms.RadioSelect, choices=BIO_CHOICES) 
    height = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    weight = forms.FloatField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    goals = forms.ChoiceField(widget=forms.RadioSelect, choices=GOALS_CHOICES)
    activity_level = forms.ChoiceField(widget=forms.Select(attrs={'class': 'form-control'}), choices=ACTIVITY_CHOICES)
    helper = FormHelper()
    helper.form_tag = False
    helper.layout = Layout(
        HTML("<h3 class=\"sr-only\">Account</h3>"),
        Fieldset('Account',
            Div(
                Div(
                    'name',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'username',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                Div(
                    'email',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'password',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                css_class="row",
            ),
            Div(
                Div(
                    'birthdate',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'genre',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                css_class="row",
            ),   
#            Div(
#                Div(
#                    'profile_picture',
#                    css_class="col-sm-4 col-sm-offset-1",
#                ),
#                css_class="row",
#            ),
        ),  
        HTML("<h3 class=\"sr-only\">Fitness</h3>"),
        Fieldset('Fitness',
            Div(
                Div(
                    'training_place',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'equipment',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                css_class="row",
            ),
            Div(
                Div(
                    'chat_availability',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'fitness_bio',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                css_class="row",
            ),
        ),
        HTML("<h3 class=\"sr-only\">Body</h3>"),
        Fieldset('Body',
            Div(
                Div(
                    'height',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'weight',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                css_class="row",
            ),
            Div(
                Div(
                    'goals',
                    css_class="col-sm-4 col-sm-offset-1",
                ),
                Div(
                    'activity_level',
                    css_class="col-sm-4 col-sm-offset-2",
                ),
                css_class="row",
            ),
        )
    )