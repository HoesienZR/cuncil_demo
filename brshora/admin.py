from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Statue
# Register your models here.
@admin.register(Statue)
class brshoraadmin(ImportExportModelAdmin):
    list_display = ['date']
