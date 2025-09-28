from django.db import models

class WeeklyBalance(models.Model):
    id = models.BigIntegerField(primary_key=True)
    total = models.IntegerField()
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-createdAt']
        verbose_name = "Balance Semanal"
        verbose_name_plural = "Balances Semanales"

    def __str__(self):
        return f'Balance {self.id}'