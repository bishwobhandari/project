from django.contrib import admin
from . models import PropertyTax

from import_export.admin import ImportExportModelAdmin
# Register your models here.

# admin.site.register(PropertyTax)

@admin.register(PropertyTax)
class ViewAdmin(ImportExportModelAdmin):
    pass