# code: utf-8
from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
from django.utils import timezone


class SoftDeleteQuerySet(models.QuerySet):
    def delete(self):
        self.update(deleted=True)


class SoftDeleteManager(models.Manager):
    """
    Alternative manager for fake deleted records
    """
    use_for_related_fields = True

    def with_deleted(self):
        return SoftDeleteQuerySet(self.model, using=self._db)

    def deleted(self):
        return self.with_deleted().filter(deleted=True)

    def get_queryset(self):
        return self.with_deleted().exclude(deleted=True)


class ToDo(models.Model):
    """
    To do record model
    """
    note = models.TextField(verbose_name=u"ToDo")
    added_at = models.DateTimeField(verbose_name=u"Added At", auto_now_add=True)
    done = models.BooleanField(verbose_name=u"Done")
    done_at = models.DateTimeField(verbose_name=u"Done At", auto_now_add=True)
    deleted = models.BooleanField(verbose_name=u"Deleted")
    deleted_at = models.DateTimeField(verbose_name=u"Deleted At", null=True, blank=True, editable=False)

    def __unicode__(self):
        return u"Todo note of {} user (ID={})".format(self.user.username, self.pk)

    def delete(self, using=None, keep_parents=False):
        # preventing record from deletion
        return

    objects = SoftDeleteManager()  # overriding original manager for act like fake deleted records as deleted.

    class Meta:
        verbose_name = u"Todo"
        verbose_name_plural = u"Todos"
        ordering = ['added_at', ]


@receiver(pre_delete, sender=ToDo)
def fake_delete(sender, instance, **kwargs):
    # make record looks like deleted
    instance.deleted = True
    instance.deleted_at = timezone.now()

@receiver(post_save, sender=ToDo)
def add_timestamp_at_done(sender, instance, **kwargs):
    # When done add timestamp
    if instance.done:
        instance.done_at = timezone.now()
