from django.db import models

class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    age = models.IntegerField()

    def __str__(self):
        return self.fname + ' ' +self.lname