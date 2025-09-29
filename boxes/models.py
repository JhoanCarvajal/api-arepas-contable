from django.db import models

class Box(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=255)
    icon = models.CharField(max_length=255, blank=True, null=True)
    total = models.IntegerField()
    cantPriceFields = models.BooleanField(default=False)
    createdAt = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-createdAt']
        verbose_name = "Caja"
        verbose_name_plural = "Cajas"

    def __str__(self):
        return self.name

class BoxControls(models.Model):
    id = models.BigIntegerField(primary_key=True)
    box = models.ForeignKey(Box, related_name='controls', on_delete=models.CASCADE)
    date = models.DateField()
    origin = models.CharField(max_length=100)
    quantity = models.IntegerField(null=True, blank=True)
    price = models.IntegerField(null=True, blank=True)
    total = models.IntegerField()
    note = models.TextField(blank=True, null=True)
    createdAt = models.DateTimeField(auto_now_add=True)
    updatedAt = models.DateTimeField(auto_now=True)
    deletedAt = models.DateTimeField(null=True, blank=True)

    class Meta:
        ordering = ['-date']
        verbose_name = "Control de Caja"
        verbose_name_plural = "Controles de Caja"

    def __str__(self):
        return f'Control para {self.box.name} en {self.date}'