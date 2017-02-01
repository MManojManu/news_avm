from django.contrib import admin
from .models import (ResolvedNewsType, UnresolvedNewsType, MapUnresolvedResolvedNewsType,
                     ResolvedLocation, UnresolvedLocation, MapUnresolvedResolvedLocation,
                     Source, ArticleParsed, ArticleContent, ArticleDownload, Author,
                     )


class ResolvedNewsTypeAdmin(admin.ModelAdmin):
    fields = ['resolved_news_type_name']


class UnresolvedNewsTypeAdmin(admin.ModelAdmin):
    fields = ['unresolved_news_type_name']


class MapUnresolvedResolvedNewsTypeAdmin(admin.ModelAdmin):
    fields = ['resolved_news_type', 'unresolved_news_type']


class ResolvedLocationAdmin(admin.ModelAdmin):
    fields = ['resolved_location_name']


class UnResolvedLocationAdmin(admin.ModelAdmin):
    fields = ['unresolved_location_name']


class MapUnresolvedResolvedLocationAdmin(admin.ModelAdmin):
    fields = ['resolved_location', 'unresolved_location']


class SourceAdmin(admin.ModelAdmin):
    fields = ['source_name', 'source_url']



class ArticleDownloadAdmin(admin.ModelAdmin):
    fields = ['local_file_path', 'article_download_created_date',
              'article_download_last_updated_date', 'is_parsed']


class ArticleParsedAdmin(admin.ModelAdmin):
    fields = ['article_title', 'unresolved_news_type'
              'url', 'published_date', 'created_date', 'last_updated_date',
              'unresolved_location', 'source', 'unique', 'article_download']


class ArticleContentAdmin(admin.ModelAdmin):
    fields = ['article_parsed', 'contents']


class AuthorAdmin(admin.ModelAdmin):
    fields = ['author_name', 'article_parsed']

# Register your models here.
admin.site.register(ResolvedNewsType, ResolvedNewsTypeAdmin)
admin.site.register(UnresolvedNewsType, UnresolvedNewsTypeAdmin)
admin.site.register(MapUnresolvedResolvedNewsType, MapUnresolvedResolvedNewsTypeAdmin)
admin.site.register(ResolvedLocation, ResolvedLocationAdmin)
admin.site.register(UnresolvedLocation, UnResolvedLocationAdmin)
admin.site.register(MapUnresolvedResolvedLocation, MapUnresolvedResolvedLocationAdmin)
admin.site.register(Source, SourceAdmin)
admin.site.register(ArticleDownload, ArticleDownloadAdmin)
admin.site.register(ArticleParsed, ArticleParsedAdmin)
admin.site.register(ArticleContent, ArticleContentAdmin)
admin.site.register(Author, AuthorAdmin)
