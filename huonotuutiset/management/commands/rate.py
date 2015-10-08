from django.core.management.base import BaseCommand
from django.db import transaction

from huonotuutiset.models import NewsItem, Rule
from huonotuutiset.rating import rate


class Command(BaseCommand):
    help = 'Calculate ratings for news items'

    def add_arguments(self, parser):
        parser.add_argument(
            '--all',
            action='store_true',
            dest='all',
            default=False,
            help='Update all ratings')

        parser.add_argument(
            '--test',
            dest='test',
            type=lambda s: unicode(s, 'utf8'),
            default=None,
            help='Test by rating a single string')

    @transaction.atomic
    def handle(self, *args, **options):
        rules = Rule.objects.all()

        if options['test']:
            score, matches = rate(options['test'], rules)
            self.stdout.write('score: %.1f, matches: %s' % (score, ' '.join([m.name for m in matches])))
            return

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
