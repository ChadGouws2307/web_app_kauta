from django.contrib import admin

from .models import Country, Sector, Industry, CompanyStock, CompanyFinancials


class CountryAdmin(admin.ModelAdmin):
    pass


class SectorAdmin(admin.ModelAdmin):
    pass


class IndustryAdmin(admin.ModelAdmin):
    pass


class CompanyStockAdmin(admin.ModelAdmin):
    pass


class CompanyFinancialsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Country, CountryAdmin)
admin.site.register(Sector, SectorAdmin)
admin.site.register(Industry, IndustryAdmin)
admin.site.register(CompanyStock, CompanyStockAdmin)
admin.site.register(CompanyFinancials, CompanyFinancialsAdmin)
