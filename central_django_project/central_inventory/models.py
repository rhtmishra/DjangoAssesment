from django.db import models
from django.contrib.auth.models import User

# Create your models here.



class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(
        User, 
        related_name="%(class)s_createdby",
        on_delete=models.CASCADE,
        null=True
    )
    updated_by = models.ForeignKey(
        User, 
        related_name="%(class)s_updatedby",
        on_delete=models.CASCADE,
        null=True,
    )
    class Meta:
        abstract=True

class Site(BaseModel):
    site_id = models.IntegerField(primary_key=True)
    site_name = models.CharField(max_length=100, null=False)
    address = models.CharField(max_length=100, null=False)
    state = models.CharField(max_length=100, null=True)
    country = models.CharField(max_length=100, null=False)
    zipcode = models.IntegerField(null=True)

    # def __str__(self):
    #     return self.site_name 

class Order(BaseModel):
    status = (
        ('Pending', 'Pending'),
        ('In-Transit', 'In-Transit'),
        ('Delivered', 'Delivered')
    )
    order_id = models.IntegerField(primary_key=True)
    purchase_id = models.IntegerField(null=False)
    quantity = models.IntegerField(null=False)
    type = models.CharField(max_length=50, null=False)
    csm_name = models.CharField(max_length=50, null=False)
    status = models.CharField(max_length=100, choices=status)

    # def __str__(self):
    #     return self.order_id 

class IAP(BaseModel):
    IAP_site = models.ForeignKey(
        Site, related_name='iappersite', on_delete=models.CASCADE)
    IAP_order = models.ForeignKey(
        Order, related_name='iaporder', on_delete=models.CASCADE)
    
    serial_no = models.IntegerField(primary_key=True)
    mac_address = models.CharField(max_length=100, null=False)
    ip_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=True)
    status = models.BooleanField(null=False)
    is_virtual = models.CharField(max_length=100, null=False)



class Switch(BaseModel):
    switch_site = models.ForeignKey(
        Site, related_name='switchespersite', on_delete=models.CASCADE
    )
    switch_order = models.ForeignKey(
        Order, related_name='switchorder', on_delete=models.CASCADE
    )
    serial_no = models.IntegerField(primary_key=True)
    mac_address = models.CharField(max_length=100, null=False)
    ip_address = models.CharField(max_length=100, null=False)
    model = models.CharField(max_length=100, null=True)




 
