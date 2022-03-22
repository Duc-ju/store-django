from django.db import models

# Create your models here.
class Brand(models.Model):
    name: models.CharField(max_length=255)

class MobileDevice(models.Model):
    productName = models.CharField(max_length=511)
    batteryCapacity = models.CharField(max_length=255)
    warrantyDuration = models.CharField(max_length=255)
    warrantyType = models.CharField(max_length=255)
    condition = models.CharField(max_length=255)
    screenSize = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)


class Laptop(MobileDevice):
    laptopType = models.CharField(max_length=255)
    storageType = models.CharField(max_length=255)
    weight = models.CharField(max_length=255)


class SmartPhone(MobileDevice):
    processorType = models.CharField(max_length=255)
    storageCapacity = models.CharField(max_length=255)
    mobileCableType = models.CharField(max_length=255)
    ram = models.CharField(max_length=255)


class Tablet(MobileDevice):
    eReader = models.BooleanField(default=False)
    storageCapacity = models.CharField(max_length=255)


class SmartPhoneItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    smartPhone = models.OneToOneField(SmartPhone, on_delete=models.CASCADE)


class LaptopItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    laptop = models.OneToOneField(Laptop, on_delete=models.CASCADE)


class TabletItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    tablet = models.OneToOneField(Tablet, on_delete=models.CASCADE)


class SmartPhoneItemImage(models.Model):
    smartPhoneItem = models.ForeignKey(SmartPhoneItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/smartphone_item_images/')


class TabletItemImage(models.Model):
    tabletItem = models.ForeignKey(Tablet, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/tablet_item_images/')


class LaptopItemImage(models.Model):
    laptopItem = models.ForeignKey(LaptopItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/laptop_item_images/')
