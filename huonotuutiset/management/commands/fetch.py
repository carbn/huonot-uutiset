import hashlib
import uuid
from datetime import datetime
from time import mktime

from django.core.management.base import BaseCommand, CommandError
from django.db import transaction
import feedparser
import pytz

from huonotuutiset.models import Site, NewsItem


class Command(BaseCommand):
    help = 'Fetch new news items from the RSS feeds'

    def fetch(self, url):
        feed = feedparser.parse(url)

        data = []

        for entry in feed.entries:
            item = {}

            item['']

        feed

    @transaction.atomic
    def handle(self, *args, **options):
        for site in Site.objects.all():
            self.stdout.write('Updating %s' % site.name)

            feed = feedparser.parse(site.rss_url)

            for entry in feed.entries:
                guid = uuid.UUID(bytes=hashlib.md5(entry['id']).digest())
                published = datetime.fromtimestamp(mktime(entry['published_parsed'])).replace(tzinfo=pytz.UTC)

                obj, created = NewsItem.objects.update_or_create(
                    guid=guid,
                    defaults={
                        'site': site,
                        'title': entry['title'],
                        'link': entry['link'],
                        'published': published
                    }
                )

                if created:
                    self.stdout.write('[+] Added: %s' % entry['title'])
                else:
                    self.stdout.write('[+] Updated: %s' % entry['title'])
