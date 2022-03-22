from django.db import models

# Create your models here.
from django.db import models

# Create your models here.


class Clothes(models.Model):
    productName = models.CharField(max_length=255)
    material = models.CharField(max_length=255)
    countryOfOrigin = models.CharField(max_length=255)
    size = models.CharField(max_length=255)
    pattern = models.CharField(max_length=255)
    plusSize = models.BooleanField(default=False)
    brand = models.CharField(max_length=255)


class KidClothes(Clothes):
    gender = models.CharField(max_length=255)
    recommendedAge = models.CharField(max_length=255)


class MaleClothes(Clothes):
    tallFit = models.BooleanField(default=False)


class MalePant(MaleClothes):
    length = models.FloatField()


class MaleShirt(MaleClothes):
    sleeveLength = models.FloatField()


class FemaleClothes(Clothes):
    petite = models.BooleanField(default=False)
    season = models.CharField(max_length=255)
    occasion = models.CharField(max_length=255)


class FemalePant(MaleClothes):
    bottomsLength = models.FloatField()
    waistHeight = models.FloatField()


class FemaleShirt(MaleClothes):
    neckline = models.CharField(max_length=255)
    croppedTop = models.BooleanField(default=False)
    topLength = models.FloatField()
    sleeveLength = models.FloatField()


class Dress(MaleClothes):
    length = models.FloatField()
    style = models.CharField(max_length=255)


class KidClothesItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    kidClothes = models.OneToOneField(KidClothes, on_delete=models.CASCADE)


class MalePantItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    malePant = models.ForeignKey(MalePant, on_delete=models.CASCADE)


class MaleShirtItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    maleShirt = models.OneToOneField(MaleShirt, on_delete=models.CASCADE)



class FemalePantItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    femalePant= models.OneToOneField(FemalePant, on_delete=models.CASCADE)


class FemaleShirtItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    femaleShirt = models.OneToOneField(FemaleShirt, on_delete=models.CASCADE)


class DressItem(models.Model):
    prices = models.FloatField(default=0)
    description = models.TextField(max_length=8191)
    header = models.TextField(max_length=1023)
    discount = models.FloatField(default=0)
    dress = models.OneToOneField(Dress, on_delete=models.CASCADE)


class KidClothesItemImage(models.Model):
    kidClothesItem = models.ForeignKey(KidClothesItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/kid_clothes_item_images/')


class MalePantItemImage(models.Model):
    malePantItem = models.ForeignKey(MalePantItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/male_pant_item_images/')


class MaleShirtItemImage(models.Model):
    maleShirtItem = models.ForeignKey(MaleShirtItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/male_shirt_item_images/')


class FemaleShirtItemImage(models.Model):
    femaleShirtItem = models.ForeignKey(FemaleShirtItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/female_shirt_item_images/')


class FemalePantItemImage(models.Model):
    femalePantItem = models.ForeignKey(FemalePantItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/female_pant_item_images/')


class DressItemImage(models.Model):
    dressItem = models.ForeignKey(DressItem, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/dress_item_images/')
