from django.db import models


class Site(models.Model):
    name = models.CharField(max_length=30)
    site_url = models.URLField()
    rss_url = models.URLField()

    def __unicode__(self):
        return self.name


class Rule(models.Model):
    name = models.CharField(max_length=15)
    regex = models.CharField(max_length=256)
    multiplier = models.FloatField()

    def __unicode__(self):
        return self.name + ' (' + self.regex + ')'


class NewsItem(models.Model):
    site = models.ForeignKey(Site)
    title = models.CharField(max_length=256)
    link = models.URLField(max_length=512)
    guid = models.UUIDField(primary_key=True)
    published = models.DateTimeField()
    matches = models.ManyToManyField(Rule, related_name='matches')
    score = models.FloatField(null=True)

    def __unicode__(self):
        return self.title
