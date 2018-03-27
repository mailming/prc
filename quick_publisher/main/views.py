from django.http import Http404
from django.shortcuts import render, redirect
from .models import User


def home(request):
    return render(request, 'home.html')


def verify(request, uuid):
    try:
        user = User.objects.get(verification_uuid=uuid, is_verified=False)
    except User.DoesNotExist:
        raise Http404("User does not exist or is already verified")

    user.is_verified = True
    user.save()

    return redirect('home')
