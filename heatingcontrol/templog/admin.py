from django.contrib import admin

# Register your models here.

from templog.models import Temperature, Probe
admin.site.register(Temperature)
admin.site.register(Probe)
