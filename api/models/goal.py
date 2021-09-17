from django.db import models
from django.contrib.auth import get_user_model


class Goal(models.Model):
  # define fields
  # https://docs.djangoproject.com/en/3.0/ref/models/fields/
  name = models.CharField(max_length=100)
  characters = models.IntegerField()
  language = models.CharField(max_length=100)
  # DateField() expects one of these date formats
# '2006-10-25'
# '10/25/2006'
# '10/25/06'
  date = models.DateField()
  time = models.IntegerField()
  measurement = models.CharField(max_length=100)
  frequency = models.CharField(max_length=100)
  created = models.DateTimeField(auto_now=True)
  updated = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(
      get_user_model(),
      on_delete=models.CASCADE
  )

  def __str__(self):
    # This must return a string
    return f"I want to type {self.characters} characters per minute in {self.language}, by {self.date}. I will achieve this by practicing {self.time} {self.measurement} every {self.frequency}."

  def as_dict(self):
    """Returns dictionary version of Goal models"""
    return {
        'id': self.id,
        'name': self.name,
        'characters': self.characters,
        'language': self.language,
        'date': self.date,
        'time': self.time,
        'measurement': self.measurement,
        'frequency': self.frequency,
        'created': self.created,
        'updated': self.updated,
    }
