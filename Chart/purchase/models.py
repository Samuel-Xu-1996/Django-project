from django.db import models

class Purchase(models.Model):
    Po = models.CharField('P O #', max_length=30)
    Vendor_No = models.CharField('Vendor No.', max_length=30)
    Vendor_Name = models.CharField('Vendor_Name', max_length=50)
    Line = models.CharField('Line #', max_length=50)
    Partno = models.CharField('Partno', max_length=50)
    Partdescr = models.CharField('Partdescr', max_length=50)
    GL_Accountno = models.CharField('GL_Accountno', max_length=50)
    Datepromised = models.DateField('Datepromised')
    Qtyonorder = models.IntegerField('Qtyonorder')
    Price = models.FloatField('Price')
    Line_Amount = models.IntegerField('Line_Amount')
    Requestedby = models.CharField('Requestedby', max_length=100)
    Buyer = models.CharField('Buyer', max_length=100)
    Status = models.CharField('Status', max_length=30)
    Projectno = models.CharField('Projectno', max_length=100)
    Project_Desc = models.CharField('Project_Desc', max_length=200)

    class Meta:
        verbose_name = 'purchase report'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.Vendor_No