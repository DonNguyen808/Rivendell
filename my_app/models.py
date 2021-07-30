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
    price = models.IntegerField('Price')
    size = models.CharField(("Size"), max_length=150)
    height = models.CharField(("Height"), max_length=150)

    def __str__(self):
        return f'{self.english}'

    class Meta:
        verbose_name_plural = 'Nurseries'
        db_table = 'Nursery'



# class Working_store(models.Model):
#     english=models.CharField(max_length=30)
#     spanish=models.CharField(max_length=30)
#     vietnamese=models.CharField(max_length=30)
#     price=models.IntegerField
#     size=models.CharField(max_length=30)
#     height=models.CharField(max_length=30)


#     class Meta:
#         verbose_name_plural = 'Working_store'
#         db_table='Working'

