import re

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction

from huonotuutiset.models import NewsItem, Rule
from huonotuutiset.rating import rate

class Command(BaseCommand):
    help = 'Calculate ratings for news items'

    def add_arguments(self, parser):
        parser.add_argument('--all',
            action='store_true',
            dest='all',
            default=False,
            help='Update all ratings')

    @transaction.atomic
    def handle(self, *args, **options):
        rules = Rule.objects.all()

        if options['all']:
            all_items = NewsItem.objects.all()
        else:
            all_items = NewsItem.objects.filter(score__isnull=True)

        for item in all_items:
            score, matches = rate(item.title, rules)

            item.score = score
            item.matches = matches
            item.save()

            self.stdout.write('%s' % (item.title))

            if score != 1.0:
                self.stdout.write('  score: %.1f, matches: %s' % (score, ' '.join([m.name for m in matches])))
