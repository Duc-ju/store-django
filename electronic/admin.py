from django.contrib import admin
from .models import MobilePhone, Laptop, Tablet, ElectronicItem, ElectronicItemImage
# Register your models here.
admin.site.register(MobilePhone)
admin.site.register(Laptop)
admin.site.register(Tablet)
admin.site.register(ElectronicItem)
admin.site.register(ElectronicItemImage)

