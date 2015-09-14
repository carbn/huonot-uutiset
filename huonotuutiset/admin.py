from django.contrib import admin

from .models import Site, NewsItem, Rule

class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_url', 'rss_url')
    ordering = ('name',)

class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'regex', 'multiplier')
    ordering = ('multiplier',)

admin.site.register(Site, SiteAdmin)
admin.site.register(NewsItem)
admin.site.register(Rule, RuleAdmin)
