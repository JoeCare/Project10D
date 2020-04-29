from django.db import models

# Create your models here.


class Item(models.Model):
    name = models.CharField(max_length=30)
    value = models.DecimalField(decimal_places=2, max_digits=5)
    type = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    img_url = models.CharField(max_length=30, blank=True)

    def __str__(self):
        return self.name
        # f'{self.name} from {self.location}'


"""in shell:
>>> Treasure.objects  # is a startpoint for django QuerySer - collection from db.
# QuerySet equates to SELECT in SQL
>>> Treasure.objects.all()  # equals SELECT * FROM Treasure
>>> Treasure.objects.filter(location = 'Blue River')
# (I think) equals to SELECT * FROM Treasure WHERE location='Blue River'
>>>Treasure.objects.get(pk=1)  # .get() is useful when we know unique variable for some query
"""
