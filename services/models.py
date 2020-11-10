from django.db import models


class Level(models.Model):
    name = models.CharField(max_length=50, null=False, blank=False)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name
