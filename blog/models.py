from django.conf import settings
from django.db import models
from django.utils import timezone


class Post(models.Model):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE) # this is a link to another model
    title = models.CharField(max_length=200) # this is how you define text with a limited number of characters
    text = models.TextField() # this is for long text without a limit
    created_date = models.DateTimeField(default=timezone.now) # this is a date and time
    published_date = models.DateTimeField(blank=True, null=True)    

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title