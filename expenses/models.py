from django.db import models

class Expenses(models.Model):
    id = models.BigIntegerField(primary_key=True)
    weeklyBalance = models.ForeignKey('weeklybalances.WeeklyBalance', on_delete=models.SET_NULL, related_name='expenses', null=True, blank=True)
    date = models.DateField()
    earnings = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    totalExpenses = models.IntegerField()
    netProfit = models.IntegerField()
    deletedAt = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Gasto"
        verbose_name_plural = "Gastos"

    def __str__(self):
        return f'Gasto para {self.date}'