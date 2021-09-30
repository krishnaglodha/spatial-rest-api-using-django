from django.contrib.gis.db import models
# from django.db import models

# Create your models here.
class pokemoncenters(models.Model):
    name = models.CharField(max_length=50)
    master  = models.CharField(max_length=50)
    rating = models.IntegerField()
    location = models.PointField(srid=4326,null=True,blank=True)


    def __str__(self):
        return self.name
