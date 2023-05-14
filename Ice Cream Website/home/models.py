from django.db import models

# Create your models here.
# Basically tables

class Contact(models.Model):
    name = models.CharField(("name"), max_length=120)
    email = models.EmailField(("email"), max_length=254)
    phone = models.CharField(("phone"), max_length=12)
    desc = models.TextField(("desc"))

    def __str__(self):
        return self.name
    


