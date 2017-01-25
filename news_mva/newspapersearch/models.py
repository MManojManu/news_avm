from __future__ import unicode_literals

from django.db import models
from datetime import datetime

class resolved_news_type(models.Model):
    resolved_news_type_name = models.CharField(max_length=250, unique=True)


class unresolved_news_type(models.Model):
    unresolved_news_type_name = models.CharField(max_length=250)


class map_unresolved_resolved_news_type(models.Model):
    resolved_news_type = models.ForeignKey(resolved_news_type, on_delete=models.DO_NOTHING)
    unresolved_news_type = models.ForeignKey(unresolved_news_type, on_delete=models.DO_NOTHING, unique=True)


class resolved_location(models.Model):
    resolved_location_name = models.CharField(max_length=250, unique=True)


class unresolved_location(models.Model):
    unresolved_location_name = models.CharField(max_length=250)


class map_unresolved_resolved_location(models.Model):
    resolved_location = models.ForeignKey(resolved_location, on_delete=models.DO_NOTHING)
    unresolved_location = models.ForeignKey(unresolved_location, on_delete=models.DO_NOTHING, unique=True)


class source(models.Model):
    source_name = models.CharField(max_length=250, unique=True)
    source_url = models.CharField(max_length=250)


class article_download(models.Model):
    local_file_path = models.CharField(max_length=250)
    article_download_created_date = models.DateTimeField(default=datetime.now)
    article_download_last_updated_date = models.DateTimeField(default=datetime.now)
    is_parsed = models.SmallIntegerField


class article_parsed(models.Model):
    article_title = models.CharField(max_length=250)
    unresolved_news_type = models.ForeignKey(unresolved_news_type, on_delete=models.DO_NOTHING)
    url = models.CharField(max_length=250)
    published_date = models.DateTimeField(default=datetime.now)
    created_date = models.DateTimeField(default=datetime.now)
    last_updated_date = models.DateTimeField(default=datetime.now)
    unresolved_location = models.ForeignKey(unresolved_location, on_delete=models.DO_NOTHING)
    source = models.ForeignKey(source, on_delete=models.DO_NOTHING)
    unique = models.CharField(max_length=250)
    article_download = models.ForeignKey(article_download, on_delete=models.DO_NOTHING)


class article_content(models.Model):
    article_parsed = models.ForeignKey(article_parsed, on_delete=models.DO_NOTHING)
    contents = models.TextField(max_length=1)


class author(models.Model):
    author_name = models.CharField(max_length=250)
    article_parsed = models.ForeignKey(article_parsed, on_delete=models.DO_NOTHING)
