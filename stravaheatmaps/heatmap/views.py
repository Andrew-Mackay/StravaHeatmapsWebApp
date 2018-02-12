from django.shortcuts import render, redirect
from registration.backends.simple.views import RegistrationView
from django.http import HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User
from heatmap.models import UserProfile, Activity, Point
from django.views.generic.edit import FormView
from .forms import GpxUploadForm

# Create your views here.
def index(request):
    context_dict = {}
    try:
        user = User.objects.get(id=request.user.id)
        userprofile = UserProfile.objects.get_or_create(user=user)[0]
        context_dict['userprofile'] = userprofile

    except User.DoesNotExist:
        pass


    print(UserProfile.objects.all())
    print(Activity.objects.all())
    print(Point.objects.all())
    userprof = UserProfile.objects.get(id=request.user.id)
    print(userprof)

    return render(request, "index.html", context=context_dict)


def upload(request):
    form = GpxUploadForm(request.POST, request.FILES)

    userprofile = UserProfile.objects.get_or_create(user=User.objects.get(id=request.user.id))[0]
    if request.method == 'POST':
        files = request.FILES.getlist('file_field')
        if form.is_valid():
            for f in files:
                new_activity= Activity.objects.create(creator=userprofile)
                new_activity.save()

                # parse files
                # create model
                print(f)

        else:
            print("invalid form")

        return redirect('index')


    return render(request, 'upload.html', {'form': form})
