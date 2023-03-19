from datetime import datetime
from unicodedata import category
from django.db import models
from django.utils import timezone

# Create your models here.
'''''
class Employees(models.Model):
    code = models.CharField(max_length=100,blank=True) 
    firstname = models.TextField() 
    middlename = models.TextField(blank=True,null= True) 
    lastname = models.TextField() 
    gender = models.TextField(blank=True,null= True) 
    dob = models.DateField(blank=True,null= True) 
    contact = models.TextField() 
    address = models.TextField() 
    email = models.TextField() 
#   department_id = models.ForeignKey(Department, on_delete=models.CASCADE) 
#   position_id = models.ForeignKey(Position, on_delete=models.CASCADE) 
    date_hired = models.DateField() 
    salary = models.FloatField(default=0) 
    status = models.IntegerField() 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.firstname + ' ' +self.middlename + ' '+self.lastname + ' '
'''
class Category(models.Model):
    name = models.TextField()
    description = models.TextField()
    status = models.IntegerField(default=1) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 

    def __str__(self):
        return self.name

class Material(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(blank=True, null=True)
    supplier = models.CharField(max_length=50, blank=True, null=True)
    cost = models.FloatField(default=0)
    status = models.BooleanField(default=True)
    stock = models.PositiveIntegerField(default=0)
    def __str__(self):
        return self.name
    
class Products(models.Model):
    code = models.CharField(max_length=100)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.TextField()
    description = models.TextField()
    price = models.FloatField(default=0) 
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True)
    materials = models.ManyToManyField("Material", through='ProductMaterial', related_name='products')
    status = models.BooleanField(default=True)

    def __str__(self):
        return self.code + " - " + self.name

class ProductMaterial(models.Model):
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    status = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.product} - {self.material} ({self.quantity})"

class Sales(models.Model):
    code = models.CharField(max_length=100,default = 'Not have')
    sub_total = models.FloatField(default=0)
    grand_total = models.FloatField(default=0)
    tax_amount = models.FloatField(default=0)
    tax = models.FloatField(default=0)
    tendered_amount = models.FloatField(default=0)
    amount_change = models.FloatField(default=0)
    date_added = models.DateTimeField(default=timezone.now) 
    date_updated = models.DateTimeField(auto_now=True) 
    def __str__(self):
        return self.code

class salesItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)

class Bills(models.Model):
    text = models.DateTimeField(default=timezone.now) 
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    checkout = models.BooleanField(default=False)
    itemcount = models.IntegerField(default=0)
    def __str__(self) -> str:
        return self.id 
    
class billItems(models.Model):
    sale_id = models.ForeignKey(Sales,on_delete=models.CASCADE)
    product_id = models.ForeignKey(Products,on_delete=models.CASCADE)
    price = models.FloatField(default=0)
    qty = models.FloatField(default=0)
    total = models.FloatField(default=0)

