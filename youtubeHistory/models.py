from django.db import models
from django.utils import timezone

class HistoryEntry(models.Model):
    url = models.CharField(max_length=100)
    date_added = models.DateTimeField(default=timezone.now)
    annotation = models.TextField()

    def __str__(self):
        return self.annotation
