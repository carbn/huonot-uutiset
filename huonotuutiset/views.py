from datetime import datetime, timedelta

from django.shortcuts import render
from django.db.models import Avg, Count, Sum, Case, When, IntegerField
from django.utils import timezone
from isoweek import Week

from huonotuutiset.models import Site, NewsItem


def home(request, year=None, week=None):
    if not year or not week:
        # use previous week by default
        week = Week.thisweek() - 1
    else:
        week = Week(int(year), int(week))

    date_range = get_date_range(week)

    # absolute worst titles
    worst_titles = NewsItem.objects.filter(published__range=date_range, score__isnull=False).order_by('-score')[:5]

    # worst sites on average
    site_avg = Site.objects.filter(
        newsitems__published__range=date_range,
        newsitems__score__isnull=False
        ).annotate(
        score=Avg('newsitems__score')
        ).order_by('-score')[:5]

    # biggest percentage of bad titles
    sites = Site.objects.filter(
        newsitems__published__range=date_range,
        newsitems__score__isnull=False
        ).annotate(
        bad=Sum(Case(When(newsitems__score__gt=1.0, then=1), output_field=IntegerField())),
        total=Count('newsitems__score'),
        )

    percentages = []

    # calculate percentages
    for site in sites:
        bad = float(site.bad if site.bad else 0)
        total = float(site.total if site.total else 0)

        percentage = int((bad/total)*100)

        percentages.append((percentage, site))

    # sort by percentage and take top 5
    percentages = list(reversed(sorted(percentages, key=lambda x: x[0])))[:5]

    context = {
        'worst_titles': worst_titles,
        'site_avg': site_avg,
        'bad_percentages': percentages,
        'date_range': {
            'week': week,
            'start': date_range[0].date(),
            'end': date_range[1].date(),
        }
    }

    return render(request, 'home.html', context)


def site(request, id):
    site = Site.objects.get(id=id)

    context = {
        'site': site,
    }

    return render(request, 'site.html', context)


def get_date_range(week):
    start = timezone.make_aware(datetime.fromordinal(week.monday().toordinal()))
    end = start + timedelta(weeks=1)

    return [start, end]
