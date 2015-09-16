from django.shortcuts import render
from django.db.models import Avg

from huonotuutiset.models import Site


def home(request):
    context = {
        'sites': Site.objects.annotate(score=Avg('newsitems__score')).order_by('-score')
    }
    return render(request, 'home.html', context)
