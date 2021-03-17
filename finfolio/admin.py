from django.contrib import admin
from finfolio.models import Trade, TradeFile


class TradeAdmin(admin.ModelAdmin):
    pass


class TradeFileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Trade, TradeAdmin)
admin.site.register(TradeFile, TradeFileAdmin)
