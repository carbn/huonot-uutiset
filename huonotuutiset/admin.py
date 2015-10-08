from django.contrib import admin

from .models import Site, NewsItem, Rule


class SiteAdmin(admin.ModelAdmin):
    list_display = ('name', 'site_url', 'rss_url')
    ordering = ('name',)


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'score', 'published')
    list_filter = ('matches',)
    ordering = ('-published',)
    search_fields = ('title',)
    readonly_fields = ('score', 'matches',)


class RuleAdmin(admin.ModelAdmin):
    list_display = ('name', 'regex', 'multiplier')
    ordering = ('multiplier',)


admin.site.register(Site, SiteAdmin)
admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(Rule, RuleAdmin)
