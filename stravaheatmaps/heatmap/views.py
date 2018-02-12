from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from heatmap.models import UserProfile, Activity
from django.views.generic.edit import FormView
from .forms import GpxUploadForm
from django.contrib.auth.decorators import login_required
#import re
#import xml.etree.ElementTree as ET
#import gpxpy


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



# def parseFile(file):
#     points = []
#     for line in file:
#         if "<trkpt lat=" in str(line):
#             lat = float(line.split()[1][5:-2])
#             lng = float(line.split()[2][5:-2])
#             points.append((lat,lng))
#
#     return points

@login_required
def upload(request):
    form = GpxUploadForm(request.POST, request.FILES)

    userprofile = UserProfile.objects.get_or_create(user=User.objects.get(id=request.user.id))[0]
    if request.method == 'POST':
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                Activity.objects.create(creator=userprofile, gpxFile=f).save()
                # points = parseFile(f)
                # for point in points:
                #     Point.objects.create(activity=new_activity, lat=point[0], lng=point[1]).save()
                #
                # new_activity.save()
        else:
            print("invalid form")

        return redirect('index')


    return render(request, 'upload.html', {'form': form})
