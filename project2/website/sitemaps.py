# sitemaps.py
from django.contrib import sitemaps
from django.urls import reverse


class StaticViewSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = "daily"

    def items(self):
        return ["website:home_page", "website:about_page", "website:contact_page"]

    def location(self, item):
        return reverse(item)