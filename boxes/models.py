from django.db import models

class Box(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    createdAt = models.DateTimeField()

    class Meta:
        ordering = ['-createdAt']
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"

    def __str__(self):
        return self.name

class Record(models.Model):
    id = models.BigIntegerField(primary_key=True)
    box = models.ForeignKey(Box, related_name='records', on_delete=models.CASCADE)
    date = models.DateTimeField()
    createdAt = models.DateTimeField()
    origin = models.CharField(max_length=100)
    extraFields = models.JSONField(null=True, blank=True)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=15, decimal_places=2)
    total = models.DecimalField(max_digits=15, decimal_places=2)
    note = models.TextField(blank=True, null=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Registro"
        verbose_name_plural = "Registros"

    def __str__(self):
        return f'Registro para {self.box.name} en {self.date}'