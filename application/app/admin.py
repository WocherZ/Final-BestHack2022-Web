from django.contrib import admin

from .models import *


class ExtendedUserAdmin(admin.ModelAdmin):
    pass


admin.site.register(ExtendedUser, ExtendedUserAdmin)


class NewsCategoriesAdmin(admin.ModelAdmin):
    pass


admin.site.register(NewsCategories, NewsCategoriesAdmin)


class SourcesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Sources, SourcesAdmin)


class NewsAdmin(admin.ModelAdmin):
    pass


admin.site.register(News, NewsAdmin)


class CurrenciesAdmin(admin.ModelAdmin):
    pass


admin.site.register(Currencies, CurrenciesAdmin)


class CurrenciesRatesAdmin(admin.ModelAdmin):
    pass


admin.site.register(CurrenciesRates, CurrenciesRatesAdmin)


class UserPropertiesAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserProperties, UserPropertiesAdmin)


class OrganizationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(Organizations, OrganizationsAdmin)


class BalanceOperationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(BalanceOperations, BalanceOperationsAdmin)


class BuySellOperationsAdmin(admin.ModelAdmin):
    pass


admin.site.register(BuySellOperations, BalanceOperationsAdmin)

