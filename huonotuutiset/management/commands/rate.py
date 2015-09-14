import re

from django.core.management.base import BaseCommand, CommandError

from huonotuutiset.models import Site, NewsItem, Rule


class Command(BaseCommand):
    help = 'Calculate ratings for news items'

    def handle(self, *args, **options):
        rules = Rule.objects.all()

        for item in NewsItem.objects.all():
            score = 1.0
            matches = []

            for rule in rules:
                if re.search(rule.regex, item.title, re.IGNORECASE|re.UNICODE):
                    score *= rule.multiplier
                    matches.append(rule.name)

            if score != 1.0:
                self.stdout.write('%s' % (item.title))
                self.stdout.write('  score: %.1f, matches: %s' % (score, ' '.join(matches)))
