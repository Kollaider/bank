from django.contrib import admin

from app.models import Manufacturer, LoanApplication, Contract, Product


admin.site.register(Manufacturer)
admin.site.register(LoanApplication)
admin.site.register(Contract)
admin.site.register(Product)
