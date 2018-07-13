from django.db import models

class GeneralInformation(models.Model):
    chamber_name = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    year = models.IntegerField()
    census = models.IntegerField()
    scrutinized = models.FloatField()
    valid_votes = models.IntegerField()
    abstentions = models.IntegerField()
    blank_votes = models.IntegerField()
    null_votes = models.IntegerField()

    class Meta:
        ordering = ('year', 'place', 'chamber_name',)
    