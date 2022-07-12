from django.contrib import admin

from house.models import Plot
from house.models import Room
from house.models import House
from house.models import Tenant
from house.models import RoomType
from house.models import HouseType

# Register your models here.

admin.site.register(Plot)
admin.site.register(Room)
admin.site.register(House)
admin.site.register(Tenant)
admin.site.register(RoomType)
admin.site.register(HouseType)