from django.shortcuts import render
from django.db.models import Avg, Count

from huonotuutiset.models import Site, NewsItem


def home(request):
    context = {
        'worst_titles': NewsItem.objects.filter(score__isnull=False).order_by('-score')[:3],
        'worst_sites_avg': Site.objects.filter(newsitems__score__isnull=False).annotate(score=Avg('newsitems__score')).order_by('-score')[:3],
        'worst_sites_abs': Site.objects.filter(newsitems__score__gt=1.0).annotate(bad_count=Count('newsitems__score')).order_by('-bad_count')[:3],
    }

    return render(request, 'home.html', context)
