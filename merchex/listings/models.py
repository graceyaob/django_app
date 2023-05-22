from django.db import models

class Band(models.Model):
    name = models.CharField(max_length=100)
    biography = models.fields.CharField(max_length=1000)
    year_formed = models.fields.IntegerField()
    active = models.fields.BooleanField(default=True)
    official_homepage = models.fields.URLField(null=True, blank=True) 

    #Nous avons créé la classeGenre, définissant les choix qui peuvent être utilisés pour le champ genre. Genre est une classe imbriquée 
    
    class Genre(models.TextChoices):
        HIP_HOP = 'HH'
        SYNTH_POP = 'SP'
        ALTERNATIVE_ROCK = 'AR'

    genre = models.fields.CharField(choices=Genre.choices, max_length=5) 

    def __str__(self):
        return f'{self.name}'

class Listing(models.Model):
    titre = models.CharField(max_length= 100)
