from django.db import models

# Create your models here.

class Voting(models.Model):
    text = models.CharField(
               "Otazka", max_length=96, 
                blank=False)
    is_active = models.BooleanField(
               "Je aktivni", default=True, blank=False)
                
    def __str__(self):
        return self.text

class Answer(models.Model):
    voting = models.ForeignKey(Voting,
                    related_name='answers')
    text = models.CharField(
               "Otazka", max_length=96, 
                blank=False)
    count = models.IntegerField(
                "Pocet odpovedi", default=0, blank=False)

