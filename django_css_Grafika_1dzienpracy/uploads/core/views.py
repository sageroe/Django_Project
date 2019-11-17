from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from scipy import stats

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
    print('Analiza danych')
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
