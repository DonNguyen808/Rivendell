from django.contrib import admin
from .models import Search, Nursery
from import_export.admin import ImportExportModelAdmin

# Register your models here.
admin.site.register(Search)

@admin.register(Nursery)
class nursery_database(ImportExportModelAdmin):
    pass 