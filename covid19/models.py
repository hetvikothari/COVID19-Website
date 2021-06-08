from django.db import models

# Create your models here.


class Case(models.Model):
    sno = models.IntegerField()
    state_name = models.CharField(max_length=100)
    active = models.IntegerField()
    positive = models.IntegerField()
    cured = models.IntegerField()
    death = models.IntegerField()
    new_active = models.IntegerField()
    new_positive = models.IntegerField()
    new_cured = models.IntegerField()
    new_death = models.IntegerField()
    state_code = models.IntegerField()

    def __str__(self):
        return f'{self.state_name}'
