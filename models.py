from django.db import models



class Donator(models.Model):
    donation_type = models.CharField(max_length=100)
    amount = models.IntegerField()

    # person details
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    email = models.EmailField()
    mobile = models.IntegerField()
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return self.fname +" "+self.lname
