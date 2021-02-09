from django.contrib import admin
from finfolio.models import Trade


class TradeAdmin(admin.ModelAdmin):
    pass


admin.site.register(Trade, TradeAdmin)
