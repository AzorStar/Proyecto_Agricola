from os import times
from django.contrib import admin
from prinapp.models import *
# Register your models here.
admin.site.register(client)
admin.site.register(supplier)
admin.site.register(product)
admin.site.register(driver)
admin.site.register(time)
admin.site.register(reports)
