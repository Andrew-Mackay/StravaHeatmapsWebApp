from django.shortcuts import render
from registration.backends.simple.views import RegistrationView
from django.http import HttpResponse
from django.core.urlresolvers import reverse

# Create your views here.
def index(request):
    return render(request, "index.html")
