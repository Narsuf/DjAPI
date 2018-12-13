from django.db import models
    
class Election(models.Model):
    year = models.IntegerField()
    name = models.CharField(max_length=30)
    place = models.CharField(max_length=50)
    chamber_name = models.CharField(max_length=30)
    total_elects = models.IntegerField()
    scrutinized = models.FloatField()
    valid_votes = models.IntegerField()
    abstentions = models.IntegerField()
    blank_votes = models.IntegerField()
    null_votes = models.IntegerField()

    class Meta: 
        ordering = ('year', 'name', 'place', 'chamber_name')

class Party(models.Model):
    name = models.CharField(primary_key=True, max_length=30)
    color = models.CharField(max_length=30)

    class Meta:
        ordering = ('name',)

class Results(models.Model):
    party = models.ForeignKey(Party, on_delete=models.CASCADE)
    election = models.ForeignKey(Election, on_delete=models.CASCADE)
    elects = models.IntegerField()
    votes = models.IntegerField()

    class Meta:
        unique_together = ('party', 'election')