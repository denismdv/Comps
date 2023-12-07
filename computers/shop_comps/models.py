from django.db import models

class Computers(models.Model):
    chipset = models.CharField("Процессор", max_length=40)
    ram = models.IntegerField("Оперативная память")
    videocard = models.CharField("Видеокарта", max_length=30)
    disk = models.CharField("Диск", max_length=20)
    price = models.IntegerField("Цена")
