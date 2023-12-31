from django.db import models

# Create your models here.
class Item(models.Model):
    name = models.CharField(max_length=50, null=False , blank=False)
    data = models.BooleanField(null=False , blank=False, default=False)

    def __string__(self):
        return self.name