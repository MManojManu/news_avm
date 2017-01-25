from django.contrib import admin
from .models import resolved_news_type, unresolved_news_type, map_unresolved_resolved_news_type, \
    resolved_location, unresolved_location, map_unresolved_resolved_location, \
    source, article_parsed, article_content, article_download, author

# Register your models here.
admin.site.register(resolved_news_type)
admin.site.register(unresolved_news_type)
admin.site.register(map_unresolved_resolved_news_type)
admin.site.register(resolved_location)
admin.site.register(unresolved_location)
admin.site.register(map_unresolved_resolved_location)
admin.site.register(source)
admin.site.register(article_parsed)
admin.site.register(article_content)
admin.site.register(author)
admin.site.register(article_download)