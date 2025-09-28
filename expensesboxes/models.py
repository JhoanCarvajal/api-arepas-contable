from django.db import models

class ExpensesBoxes(models.Model):
    id = models.BigIntegerField(primary_key=True)
    expense = models.ForeignKey('expenses.Expenses', on_delete=models.CASCADE)
    box = models.ForeignKey('boxes.Box', on_delete=models.CASCADE)
    boxControl = models.ForeignKey('boxes.BoxControls', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Gasto de Caja"
        verbose_name_plural = "Gastos de Caja"

    def __str__(self):
        return f'Gasto {self.expense.id} en caja {self.box.name}'