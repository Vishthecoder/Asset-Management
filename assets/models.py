from django.db import models


class Category(models.Model):
	name = models.CharField(max_length=200)
	slug = models.SlugField()
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "categories"
	
	def __str__(self):
		return self.name

class location(models.Model):
	name = models.CharField(max_length=200)
	city = models.CharField(max_length=50, default="Nagpur")
	state = models.CharField(max_length=50, default="Maharashtra")
	country = models.CharField(max_length=50, default="India")
	zipcode = models.CharField(max_length=6, default="440013")
	contact_no = models.CharField(max_length=10,default="2222244441")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "location"


	def __str__(self):
		return self.name




class Asset(models.Model):
	rfid = models.CharField(max_length = 10, unique= True,primary_key=True)
	type = models.ForeignKey(Category, on_delete=models.SET_NULL, null= True)
	name = models.CharField(max_length=200)
	purchase_date = models.DateField()
	warranty_expiry = models.DateField(null = True)
	PURCHASED_CHOICES = [ 
		("None","None"),
		("Owned","Owned"),
		("Subscription","Subscription"),
	]
	purchase_type = models.CharField(max_length=30,choices = PURCHASED_CHOICES, default="None")
	description = models.TextField(null = True)
	serial_no = models.CharField(max_length=10, unique= True)
	location = models.ForeignKey(location, on_delete=models.SET_NULL,null= True)
	image = models.ImageField(upload_to ='AssetImages/',default='index.jpg')
	STATE_CHOICES = [
		("Repair","Repair"),
		("In Use","In Use"),
		("Defective","Defective"),
		("Functional","Functional")
	]
	state = models.CharField(max_length=30,choices=STATE_CHOICES,default="Functional")
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "assets"



	def __str__(self):
		return self.name

class AssetMaintenance(models.Model):
	maintenance_id = models.CharField(max_length=10, unique=True)
	asset_id = models.OneToOneField(Asset, on_delete=models.CASCADE)
	maintenance_date = models.DateField()
	maintenance_description = models.TextField()
	maintenance_cost = models.DecimalField(max_digits=10, decimal_places=2)
	performed_by = models.CharField(max_length=200)
	created_at = models.DateTimeField(auto_now_add=True)
	modified_at = models.DateTimeField(auto_now=True)

	class Meta:
		verbose_name_plural = "Asset Maintenance"

	def __str__(self):
		return self.maintenance_id



