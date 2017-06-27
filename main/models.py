from django.db import models

class Occupation(models.Model):
    name = models.CharField(max_length=200)

    def publish(self):
        self.save()

    def __str__(self):
        return self.name

class Occupation_Detail(models.Model):
    owner_name = models.CharField(max_length= 100)
    owner_city = models.CharField(max_length= 100)
    owner_state = models.CharField(max_length=100)
    owner_address = models.CharField(max_length=100)
    password = models.CharField(max_length= 100)

    def publish(self):
        self.save()

    def __str__(self):
        return (self.owner_name, self.owner_city, self.owner_state, self.owner_address)