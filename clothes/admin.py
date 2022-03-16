from django.contrib import admin
from .models import MalePant, MaleShirt, KidClothes, FemalePant, FemaleShirt, Dress, ClothesItemImage
# Register your models here.
admin.site.register(MalePant)
admin.site.register(MaleShirt)
admin.site.register(KidClothes)
admin.site.register(FemalePant)
admin.site.register(FemaleShirt)
admin.site.register(Dress)
admin.site.register(ClothesItemImage)
