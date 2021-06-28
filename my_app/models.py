from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now=True) 


    # search object
    def __str__(self):
        return '{}'.format(self.search)


    # searchs
    class Meta:
        verbose_name_plural = 'Searches'


class Nursery(models.Model):
    english = models.CharField(("English"), max_length=255)
    spanish = models.CharField(("Spanish"), max_length=255)
    vietnamese = models.CharField(("Vietnamese"), max_length=255)
    retail = models.IntegerField("Retail")
    size = models.CharField(("size"), max_length=150)
    height = models.CharField(("Height"), max_length=150)

    def __str__(self):
        return f'{self.english}'

    class Meta:
        verbose_name_plural = 'Nurseries'
    
