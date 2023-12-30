from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=250)
    ticket_fee = models.CharField(max_length=100, null=True)
    is_ticket = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_creator')
    start_time = models.TimeField(null=True)
    start_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    