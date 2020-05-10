from django.db import models

# Create your models here.

class Statelist(models.Model):
    name = models.CharField(max_length=50)
    total_confirmed_cases = models.IntegerField()
    recovered_cases = models.IntegerField()
    death = models.IntegerField()

    def __str__(self):
        return self.name +' :- '+ '  Total confirmend cases:'+ str(self.total_confirmed_cases)+ '   '+'   Total recovered cases: '+ str(self.recovered_cases)+ ' '+'   Total deaths: ' + str(self.death)


