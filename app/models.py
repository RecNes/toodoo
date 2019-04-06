# code: utf-8

from django.db import models


class ToDo(models.Model):
    """
    To do record model
    """
    note = models.TextField(verbose_name=u"ToDo")
    added_at = models.DateTimeField(verbose_name=u"Added At", auto_now_add=True)
    done = models.BooleanField(verbose_name=u"Done")
    done_at = models.DateTimeField(verbose_name=u"Done At", null=True, blank=True, auto_now=True)

    def __unicode__(self):
        return u"Todo note ID={}".format(self.pk)

    class Meta:
        verbose_name = u"Todo"
        verbose_name_plural = u"Todos"
        ordering = ['added_at', ]
