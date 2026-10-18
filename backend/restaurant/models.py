from django.db import models

# Create your models here.
class Booking(models.Model):
    name=models.CharField(max_length=100)
    no_of_guests=models.IntegerField()
    booking_date=models.DateTimeField(auto_now_add=True)
class Menu(models.Model):
    title=models.CharField(max_length=100)
    price=models.IntegerField()
    inventory=models.IntegerField()
    def get_item(self):
        return f"{self.title}:{self.price}"