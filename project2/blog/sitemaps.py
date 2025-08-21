from django.urls import reverse
from django.contrib.sitemaps import Sitemap
from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.5

    def items(self):
        return Post.objects.filter(published_status=True)

    def lastmod(self, obj):
        return obj.published_date