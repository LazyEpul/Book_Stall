from django.db.models.manager import Manager

from django.db import models


class ActivebookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=0)


class InactivebookManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_deleted=1)

# Create your models here.


class book(models.Model):
    name = models.CharField(max_length=100)
    qty = models.IntegerField()
    price = models.FloatField()
    is_publish = models.BooleanField(default=False)
    publish_date = models.DateField(null=True)
    is_deleted = models.CharField(max_length=1, default=0)
    active_books = ActivebookManager()
    inactive_books = InactivebookManager()
    objects = Manager()

    def __str__(self) -> str:
        return f'{self.__dict__}'

    class Meta:
        db_table = "book"
