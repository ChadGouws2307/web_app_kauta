from django.contrib import admin

from .models import Country, Sector, Industry, CompanyStock


class CountryAdmin(admin.ModelAdmin):
    pass


class SectorAdmin(admin.ModelAdmin):
    pass


class IndustryAdmin(admin.ModelAdmin):
    pass


class CompanyStockAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(CompanyStock, CompanyStockAdmin)
