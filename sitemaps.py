from django.contrib.sitemaps import Sitemap
from books.models import Book
class BookSitemap(Sitemap):
    changefreq='weekly'; priority=0.8
    def items(self): return Book.objects.filter(is_approved=True,status='available')
    def lastmod(self,obj): return obj.updated_at
