from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats
from django import forms

import csv
import pandas as pd


def home(request):
    print('Akinator')
    return render(request, 'home.html')


def about(request):
    print('O co chodzi?')
    return render(request, 'about.html')


def contact(request):
    print('Kontakt')
    return render(request, 'contact.html')

def data_analysis(request):

    if request.method == 'POST' and request.value['Tak']:

        print('\nWhat is `myfile`?')


        print('\nDirectly accessing `myfile` gives nothing :(')
        print(type(str(myfile.read())))
        print(str(myfile.read()))

        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        print('\nHowever, when using FileSystemStorage...')
        print('\nReading filename: %s' % filename)
        print(type(fs.open(filename)))
        print(fs.open(filename))

        print('\nOpen and preview using pandas:')
        df = pd.read_csv(fs.open(filename))
        print(df)
    return render(request, 'data_analysis.html')

def akinator(request, *args, **kwargs):
    FRUIT_CHOICES= [
    ('orange', 'Oranges'),
    ('cantaloupe', 'Cantaloupes'),
    ('mango', 'Mangoes'),
    ('honeydew', 'Honeydews'),
    ]

    class UserForm(forms.Form):
        first_name= forms.CharField(max_length=100)
        last_name= forms.CharField(max_length=100)
        email= forms.EmailField()
        age= forms.IntegerField()
        favorite_fruit= forms.CharField(label='What is your favorite fruit?', widget=forms.RadioSelect(choices=FRUIT_CHOICES))
    return render(request, "akinator.html", {})
