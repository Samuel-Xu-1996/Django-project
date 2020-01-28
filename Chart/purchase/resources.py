from import_export import resources
from .models import Purchase

class PurchaseResource(resources.ModelResource):

    class Meta:
        model = Purchase
        fields = ('Po',
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
