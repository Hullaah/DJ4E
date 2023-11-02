from django.shortcuts import render
from django.http import HttpResponse, HttpRequest

# Create your views here.
def hello_view(request: HttpRequest):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session["num_visits"] = num_visits
    if num_visits > 4:
        del request.session["num_visits"]
    resp = HttpResponse('num_visits=' + str(num_visits))
    resp.set_cookie('dj4e_cookie', '87383af6', max_age=1000)
    return resp