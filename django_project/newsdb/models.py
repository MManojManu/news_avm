from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class ResolvedNewsType(models.Model):
    resolved_news_type_name = models.CharField(max_length=250, unique=True)

    def __str__(self):
        return self.resolved_news_type_name

    class Meta:
        db_table = 'ResolvedNewsType'
        verbose_name = 'Resolved News Type'
        managed = False


class UnresolvedNewsType(models.Model):
    unresolved_news_type_name = models.CharField(max_length=250)

    def __str__(self):
        return self.unresolved_news_type_name

    class Meta:
        db_table = 'UnResolvedNewsType'
        verbose_name = 'UnResolved News Type'
        managed = False


class MapUnresolvedResolvedNewsType(models.Model):
    resolved_news_type = models.ForeignKey(ResolvedNewsType, on_delete=models.DO_NOTHING)
    unresolved_news_type = models.ForeignKey(UnresolvedNewsType, on_delete=models.DO_NOTHING, unique=True)

    def __str__(self):
        return self.resolved_news_type.resolved_news_type_name

    class Meta:
        db_table = 'MapUnresolvedResolvedNewsType'
        verbose_name = 'Map Unresolved Resolved News Type'
        managed = False


class ResolvedLocation(models.Model):
    resolved_location_name = models.CharField(max_length=250, unique=True)

    def get_resolved_location(self):
        return self.resolved_location_name

    class Meta:
        db_table = 'ResolvedLocation'
        verbose_name = 'Resolved Location'
        managed = False


class UnresolvedLocation(models.Model):
    unresolved_location_name = models.CharField(max_length=250)

    def get_unresolved_location(self):
        return self.unresolved_location_name

    class Meta:
        db_table = 'UnresolvedLocation'
        verbose_name = 'UnResolved Location'
        managed = False


class MapUnresolvedResolvedLocation(models.Model):
    resolved_location = models.ForeignKey(ResolvedLocation, on_delete=models.DO_NOTHING)
    unresolved_location = models.ForeignKey(UnresolvedLocation, on_delete=models.DO_NOTHING, unique=True)

    class Meta:
        db_table = 'MapUnresolvedResolvedLocation'
        verbose_name = 'Map Unresolved Resolved Location'
        managed = False


class Source(models.Model):
    source_name = models.CharField(max_length=250, unique=True)
    source_url = models.CharField(max_length=250)

    def get_source_name(self):
        return self.source_name

    class Meta:
        db_table = 'Source'
        verbose_name = 'Source'
        managed = False


class ArticleDownload(models.Model):
    local_file_path = models.CharField(max_length=250)
    article_download_created_date = models.DateTimeField(default=datetime.now)
    article_download_last_updated_date = models.DateTimeField(default=datetime.now)
    is_parsed = models.SmallIntegerField

    class Meta:
        db_table = 'ArticleDownload'
        verbose_name = 'Article Download'
        managed = False


class ArticleParsed(models.Model):
    article_title = models.CharField(max_length=250)
    unresolved_news_type = models.ForeignKey(UnresolvedNewsType, on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)
    last_updated_date = models.DateTimeField(default=datetime.now)
    unresolved_location = models.ForeignKey(UnresolvedLocation, on_delete=models.DO_NOTHING)
    source = models.ForeignKey(Source, on_delete=models.DO_NOTHING)
    unique = models.CharField(max_length=250)
    article_download = models.ForeignKey(ArticleDownload, on_delete=models.DO_NOTHING)

    def get_article_title(self):
        return self.article_title

    class Meta:
        db_table = 'ArticleParsed'
        verbose_name = 'Article Parsed'
        managed = False


class ArticleContent(models.Model):
    article_parsed = models.ForeignKey(ArticleParsed, on_delete=models.DO_NOTHING)
    contents = models.TextField(max_length=1)

    class Meta:
        db_table = 'ArticleContent'
        verbose_name = 'Article Content'
        managed = False


class Author(models.Model):
    author_name = models.CharField(max_length=250)
    article_parsed = models.ForeignKey(ArticleParsed, on_delete=models.DO_NOTHING)

    class Meta:
        db_table = 'Author'
        verbose_name = 'Author'
        managed = False
