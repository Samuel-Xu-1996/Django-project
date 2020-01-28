from django.contrib import admin
from import_export.admin import ImportExportModelAdmin, ImportExportActionModelAdmin
from .models import Purchase
from .resources import PurchaseResource

class PurchaseAdmin(ImportExportActionModelAdmin, ImportExportModelAdmin):
    resource_class = PurchaseResource
    list_display = ('Po',
                  'Vendor_No',
                  'Vendor_Name',
                  'Line',
                  'Partno',
                  'Partdescr',
                  'GL_Accountno',
                  'Datepromised',
                  'Qtyonorder',
                  'Price',
                  'Line_Amount',
                  'Requestedby',
                  'Buyer',
                  'Status',
                  'Projectno',
                  'Project_Desc'
                  )
    list_per_page = 50


admin.site.register(Purchase, PurchaseAdmin)