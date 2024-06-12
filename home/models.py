from django.db import models

# Create your models here.
class contactInfo(models.Model):
        first_name=models.CharField(max_length=25)
        last_name=models.CharField(max_length=25)
        email=models.CharField(max_length=40)
        phone_number=models.CharField(max_length=25)
        message=models.CharField(max_length=200)
        
def __str__(self):
        return self.first_name + ' ' + self.last_name
    
class Category(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

class Product(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.TextField(max_length=100)
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE)
    description_name = models.TextField(max_length=50,blank=True, null=True)
    description = models.TextField(max_length=1000,blank=True, null=True)
    short_description = models.TextField(max_length=500,blank=True, null=True)
    feature = models.TextField(max_length=800,blank=True, null=True)
    short_feature = models.TextField(max_length=400,blank=True, null=True)
    height = models.CharField(max_length=100,blank=True, null=True)
    width = models.CharField(max_length=100,blank=True, null=True)
    depth = models.CharField(max_length=100,blank=True, null=True)
    weight = models.CharField(max_length=100,blank=True, null=True)
    security = models.CharField(max_length=800,blank=True, null=True)
    temparature = models.CharField(max_length=100,blank=True, null=True)
    displpay = models.CharField(max_length=100,blank=True, null=True)
    keyboard = models.CharField(max_length=100,blank=True, null=True)
    card_reader = models.CharField(max_length=100,blank=True, null=True)
    audio = models.CharField(max_length=100,blank=True, null=True)
    barcode_reader = models.CharField(max_length=100,blank=True, null=True)
    humidity = models.CharField(max_length=100,blank=True, null=True)
    acoustic = models.CharField(max_length=100,blank=True, null=True)
    recycling_module = models.CharField(max_length=800,blank=True, null=True)
    reciept_printer = models.CharField(max_length=100,blank=True, null=True)
    journal_printer = models.CharField(max_length=100,blank=True, null=True)
    servicing = models.CharField(max_length=200,blank=True, null=True)
    operating_platform = models.CharField(max_length=200,blank=True, null=True)
    software = models.CharField(max_length=200,blank=True, null=True)
    dispenser = models.CharField(max_length=300,blank=True, null=True)
    printer = models.CharField(max_length=300,blank=True, null=True)
    additional_feature = models.CharField(max_length=100,blank=True, null=True)
    image1=models.ImageField(upload_to="img/%y", blank=True, null=True)
    image2=models.ImageField(upload_to="img/%y", blank=True, null=True)
    image3=models.ImageField(upload_to="img/%y", blank=True, null=True)
    brochure = models.FileField(upload_to="pdf/%y", blank=True, null=True)

    def __str__(self):
        return self.title