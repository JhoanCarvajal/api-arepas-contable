from django.db import models

class History(models.Model):
    id = models.BigIntegerField(primary_key=True)
    date = models.DateTimeField()
    earnings = models.DecimalField(max_digits=15, decimal_places=2)
    createdAt = models.DateTimeField()
    generalExpenses = models.DecimalField(max_digits=15, decimal_places=2)
    operatingExpenses = models.DecimalField(max_digits=15, decimal_places=2)
    workerExpenses = models.DecimalField(max_digits=15, decimal_places=2)
    rentExpenses = models.DecimalField(max_digits=15, decimal_places=2)
    motorcycleExpenses = models.DecimalField(max_digits=15, decimal_places=2)
    cornBags = models.IntegerField()
    cornPrice = models.DecimalField(max_digits=15, decimal_places=2)
    charcoalBags = models.IntegerField()
    charcoalPrice = models.DecimalField(max_digits=15, decimal_places=2)
    totalExpenses = models.DecimalField(max_digits=15, decimal_places=2)
    netProfit = models.DecimalField(max_digits=15, decimal_places=2)

    class Meta:
        ordering = ['-date']
        verbose_name = "Historial"
        verbose_name_plural = "Historiales"

    def __str__(self):
        return f'Historial para {self.date}'