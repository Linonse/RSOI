from django.db import models

class Person(models.Model):
    person_id = models.Index
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.first_name #"%s %s" % (self.first_name, self.last_name)
# Create your models here.
