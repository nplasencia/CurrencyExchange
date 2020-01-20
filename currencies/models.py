from django.db import models

class Currency(models.Model):
    symbol = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    visible = models.BooleanField(default=True)

    def __str__(self):
        return self.symbol+'-'+self.name

