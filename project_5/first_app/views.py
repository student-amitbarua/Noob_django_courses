from django.shortcuts import render
import datetime

# Create your views here.
def home(request):
    d = {'auhtor' : 'rahim', "age" : 5, "lst" : ['python', 'is', 'best'], 'birthday' : datetime.datetime.now(), 'val' : ' ' , 'courses': [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 1,
            'name' : 'django',
            'fee' : 10000
        },
        {
            'id' : 1,
            'name' : 'java',
            'fee' : 1000
        }
    ]}
    return render(request, 'first_app/home.html', d )