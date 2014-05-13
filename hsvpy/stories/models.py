from django.db import models
from django.conf import settings

# Create your models here.
class Story(models.Model):
    title = models.CharField(max_length=255)
    created_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "Stories"

    def __unicode__(self):
        return self.title

    def last10paragraphs(self):
        """ return the last 10 paragraphs of this story"""
        return Paragraph.objects.filter(story=self)[:10]


class Paragraph(models.Model):
    story = models.ForeignKey(Story)
    text = models.TextField()
    written_by = models.ForeignKey(settings.AUTH_USER_MODEL)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('created_at', )

    def __unicode__(self):
        return self.text
