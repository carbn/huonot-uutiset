from django.core.management.base import BaseCommand, CommandError
from django.db.models import Avg

from huonotuutiset.models import Site, NewsItem


class Command(BaseCommand):
    help = 'Print hiscores'

    def handle(self, *args, **options):
        sites = Site.objects.annotate(score=Avg('newsitems__score')).order_by('score')

        for site in sites:
            self.stdout.write('%s: %f' % (site.name, site.score))
