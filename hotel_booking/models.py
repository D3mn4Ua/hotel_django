from django.db import models
from django.contrib.auth.models import User

class Room(models.Model):
    number = models.IntegerField()
    description = models.TextField()
    capacity = models.IntegerField()

    def __str__(self):
        return f"Room #{self.number}"

class Booking(models.Model):
    resident = models.ForeignKey(User, on_delete=models.CASCADE, related_name="bookings")
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name="bookings")
    booked_at = models.DateTimeField(auto_now_add=True)
    booked_from = models.DateTimeField()
    booked_till = models.DateTimeField()

    def __str__(self):
        return f"Room #{self.room.number} was booked by: {self.resident.username}"
