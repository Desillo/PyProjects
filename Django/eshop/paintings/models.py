from django.db import models
import datetime
from django.conf import settings
from django.urls import reverse
import uuid

# Create your models here.

class Author(models.Model):
    name = models.CharField(max_length=200)
    brth_date = models.DateField("birth date", blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

class Painting(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField("date published", blank=True, null=False)
    creation_date = models.DateField("date created", blank=True, null=True)
    size = models.IntegerField(blank=True, null=True)
    autor = models.ManyToManyField(Author, blank=True)
    status = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.title
    
    def clean(self):
        if self.pub_date is None:
            self.pub_date = datetime.datetime.now()

    def get_absolute_url(self):
        return reverse('painting-detail', args=[str(self.id)])



class PaintingInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    painting = models.ForeignKey('Painting', on_delete=models.RESTRICT, null=True)
    amount = models.IntegerField()
    buyer = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f'{self.id} {self.painting.title}'
    

