from django.shortcuts import render
from .models import Link


def index(request):
    watch = Link.objects.filter(watch=True).order_by('-number')
    return render(request, 'links/links.html', context={'watch':watch})

