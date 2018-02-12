from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from heatmap.models import UserProfile

# Create your views here.
def index(request):
    context_dict = {}
    try:
        user = User.objects.get(id=request.user.id)
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        context_dict['userprofile'] = userprofile

    except User.DoesNotExist:
        pass

    return render(request, "index.html", context=context_dict)
