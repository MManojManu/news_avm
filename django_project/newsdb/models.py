from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class ResolvedNewsType(models.Model):
    resolved_news_type_name = models.CharField(max_length=250)

    def __str__(self):
        return self.resolved_news_type_name

    class Meta:
        db_table = 'resolved_news_type'
        verbose_name = 'Resolved News Type'
        managed = False


class UnresolvedNewsType(models.Model):
    unresolved_news_type_name = models.CharField(max_length=250)

    def __str__(self):
        return self.unresolved_news_type_name

    class Meta:
        db_table = 'unresolved_news_type'
        verbose_name = 'UnResolved News Type'
        managed = False


class MapUnresolvedResolvedNewsType(models.Model):
    resolved_news_type = models.ForeignKey(ResolvedNewsType,
                                           on_delete=models.DO_NOTHING)
    unresolved_news_type = models.ForeignKey(UnresolvedNewsType,
                                             on_delete=models.DO_NOTHING, unique=True)

    def __str__(self):
        return self.resolved_news_type.resolved_news_type_name

    class Meta:
        db_table = 'map_unresolved_resolved_news_type'
        verbose_name = 'Map Unresolved Resolved News Type'
        managed = False


class ResolvedLocation(models.Model):
    resolved_location_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.resolved_location_name

    class Meta:
        db_table = 'resolved_location'
        verbose_name = 'Resolved Location'
        managed = False


class UnresolvedLocation(models.Model):
    unresolved_location_name = models.CharField(max_length=250)

    def __str__(self):
        return self.unresolved_location_name

    class Meta:
        db_table = 'unresolved_location'
        verbose_name = 'UnResolved Location'
        managed = False


class MapUnresolvedResolvedLocation(models.Model):
    resolved_location = models.ForeignKey(ResolvedLocation, on_delete=models.DO_NOTHING)
    unresolved_location = models.ForeignKey(UnresolvedLocation,
                                            on_delete=models.DO_NOTHING, unique=True)

    def __str__(self):
        return self.resolved_location.resolved_location_name

    class Meta:
        db_table = 'map_unresolved_resolved_location'
        verbose_name = 'Map Unresolved Resolved Location'
        managed = False


class Source(models.Model):
    source_name = models.CharField(max_length=250, unique=True)
    source_url = models.CharField(max_length=250)

    def __str__(self):
        return self.source_name

    class Meta:
        db_table = 'source'
        verbose_name = 'Source'
        managed = False


class ArticleDownload(models.Model):
    local_file_path = models.CharField(max_length=250)
    article_download_created_date = models.DateTimeField(default=datetime.now)
    article_download_last_updated_date = models.DateTimeField(default=datetime.now)
    is_parsed = models.SmallIntegerField(max_length=1)

    def __int__(self):
        return self.local_file_path

    class Meta:
        db_table = 'article_download'
        verbose_name = 'Article Download'
        managed = False


class ArticleParsed(models.Model):
    article_title = models.CharField(max_length=250)
    unresolved_news_type = models.ForeignKey(UnresolvedNewsType,
                                             on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)
    last_updated_date = models.DateTimeField(default=datetime.now)
    unresolved_location = models.ForeignKey(UnresolvedLocation,
                                            on_delete=models.DO_NOTHING)
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING)
    unique_id = models.CharField(max_length=250)
    article_download = models.ForeignKey(ArticleDownload, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.article_title

    class Meta:
        db_table = 'article_parsed'
        verbose_name = 'Article Parsed'
        managed = False


class ArticleContent(models.Model):
    article_parsed = models.ForeignKey(ArticleParsed, on_delete=models.DO_NOTHING)
    content = models.TextField()

    def __str__(self):
        return self.article_parsed.article_title

    class Meta:
        db_table = 'article_content'
        verbose_name = 'Article Content'
        managed = False


class Author(models.Model):
    author_name = models.CharField(max_length=250)
    article_parsed = models.ForeignKey(ArticleParsed, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.author_name

    class Meta:
        db_table = 'author'
        verbose_name = 'Author'
        managed = False
