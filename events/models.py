from django.db import models
from django.contrib.auth.models import User

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    location = models.CharField(max_length=250)
    ticket_fee = models.CharField(max_length=100, null=True)
    regular =  models.CharField(max_length=100, null=True)
    vip =  models.CharField(max_length=100, null=True)
    vvip =  models.CharField(max_length=100, null=True)
    is_ticket = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='event_creator')
    start_time = models.TimeField(null=True)
    start_date = models.DateField(null=True)
    end_time = models.TimeField(null=True)
    end_date = models.DateField(null=True)
    date_created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title
    
    
class Attendee(models.Model):
    event = models.ManyToManyField(Event, blank=False)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    mobile_number = models.CharField(max_length=11)
    gender = models.CharField(max_length=20)
    payment_status = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return self.name
    