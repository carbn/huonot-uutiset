import hashlib
import uuid
from datetime import datetime
from time import mktime

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction, DataError
import feedparser
import pytz

from huonotuutiset.models import Site, NewsItem


class Command(BaseCommand):
    help = 'Fetch new news items from the RSS feeds'

    @transaction.atomic
    def handle(self, *args, **options):
        for site in Site.objects.all():
            self.stdout.write('Updating %s' % site.name)

            feed = feedparser.parse(site.rss_url)

            for entry in feed.entries:
                required_keys = ['id', 'published_parsed', 'title', 'link']

                if not set(entry.keys()).issuperset(required_keys):
                    self.stderr.write('WARNING: missing fields in the entry: %s' % (entry.keys()))
                    continue

                guid = uuid.UUID(bytes=hashlib.md5(entry['id']).digest())
                published = datetime.fromtimestamp(mktime(entry['published_parsed'])).replace(tzinfo=pytz.UTC)

                try:
                    obj, created = NewsItem.objects.update_or_create(
                        guid=guid,
                        defaults={
                            'site': site,
                            'title': entry['title'],
                            'link': entry['link'],
                            'published': published
                        }
                    )
                except DataError as e:
                    self.stderr.write('ERROR: failed to update %s: %s' % (site.name, str(e)))
                    continue

                if created:
                    self.stdout.write('[+] Added: %s' % entry['title'])
                else:
                    self.stdout.write('[+] Updated: %s' % entry['title'])
