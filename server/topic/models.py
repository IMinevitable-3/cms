from django.db import models
from django import forms 

from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel , InlinePanel
from wagtail.search import index

from wagtail.api import APIField
from wagtail.documents.models import Document
from modelcluster.fields import ParentalKey
from wagtail.models import Orderable

class TopicIndexPage(Page):
    intro = RichTextField(
        blank=False, 
        help_text="Write a Topic name", 
        verbose_name="Topic Name",
    )

    content_panels = Page.content_panels + [FieldPanel("intro")]

    subpage_types = ["topic.SubTopicIndexPage"]

    api_fields = [
        APIField('intro'),
    ]

class SubTopicIndexPage(Page):
    intro = RichTextField(
        blank=False, help_text="Write a Sub Topic name", verbose_name="SubTopic Name"
    )

    content_panels = Page.content_panels + [FieldPanel("intro")]

    subpage_types = ["topic.TopicPage"]
    parent_page_types = ["topic.TopicIndexPage"]

    api_fields = [
        APIField('intro'),
    ]


class TopicPage(Page):
    intro = models.CharField(
        max_length=250, help_text="Write Heading of Sub Topic", verbose_name="Heading"
    )
    body = RichTextField(
        blank=True,
        help_text="Write Description about Sub Topic",
        verbose_name="Description",
    )
    search_fields = Page.search_fields + [
        index.SearchField("intro"),
        index.SearchField("body"),
    ]

    content_panels = Page.content_panels + [
        FieldPanel("intro"),
        FieldPanel("body"),
        InlinePanel('related_links', heading="Related links", label="Related link"),
    ]

    parent_page_types = ["topic.SubTopicIndexPage"]

    api_fields = [
        APIField('intro'),
        APIField('body'),
        APIField('TopicPageRelatedLink')
    ]


class TopicPageRelatedLink(Orderable):
    page = ParentalKey(TopicPage, on_delete=models.CASCADE, related_name='related_links')
    document = models.ForeignKey(Document, on_delete=models.CASCADE)
    panels = [
        FieldPanel('document'),
    ]