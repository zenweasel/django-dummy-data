from django.contrib import admin
from destination.models import City, Destination, DestinationCity
from django.contrib.gis.admin import OSMGeoAdmin


class DestinationAdmin(OSMGeoAdmin):
    model = Destination


class DestinationInline(admin.StackedInline):
    model = DestinationCity


class CityAdmin(OSMGeoAdmin):
    model = City
    inlines = [
        DestinationInline
    ]


admin.site.register(Destination, DestinationAdmin)
admin.site.register(City, CityAdmin)

