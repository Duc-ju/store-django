from django.contrib import admin
from .models import SmartPhone, Tablet, Laptop, SmartPhoneItem, TabletItem, LaptopItem, SmartPhoneItemImage, TabletItemImage, LaptopItemImage
# Register your models here.
admin.site.register(SmartPhone)
admin.site.register(Tablet)
admin.site.register(Laptop)
admin.site.register(SmartPhoneItem)
admin.site.register(TabletItem)
admin.site.register(LaptopItem)
admin.site.register(SmartPhoneItemImage)
admin.site.register(TabletItemImage)
admin.site.register(LaptopItemImage)

