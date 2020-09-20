from django.db import models

# Create your models here.
class Zespol(models.Model):
    ilosc_czlonkow = models.SmallIntegerField()
    # manager = models.TextChoices()
    min_kwota_zlecenia = models.SmallIntegerField()
    samochod = models.CharField(max_length=200)
    spalanie_samochodu = models.FloatField()
    fundusz = models.SmallIntegerField()

    def __str__(self):
        return f"Ilość członków: {self.ilosc_czlonkow} " \
               f"Manager: {self.manager} " \
               f"Minimalna kwota, za którą gramy: {self.min_kwota_zlecenia}" \
               f"Samochód: {self.samochod}" \
               f"Spalanie samochodu: {self.spalanie_samochodu}" \
               f"Fundusz zespołu: {self.fundusz}"

