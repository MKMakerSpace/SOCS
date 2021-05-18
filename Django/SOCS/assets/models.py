import uuid
from django.db import models



# Create your models here.

class Asset(models.Model):
	#Fields
	AssetID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	Name = models.CharField(max_length=50, help_text='Item Name')
	Manufacturer = models.CharField(max_length=50, help_text='Manufacturer Name', blank=True)
	Model = models.CharField(max_length=50, help_text='Manufacturer Model', blank=True)
	SerialNo = models.CharField(max_length=50, help_text='Model Serial Number', blank=True)
	Location = models.CharField(max_length=50, help_text='Location Stored/Kept in space')
	Owner = models.CharField(max_length=50, help_text='Owner')
	Description = models.CharField(max_length=200, help_text='Item Description')
	Notes = models.CharField(max_length=200, help_text='Item Notes', blank=True)
	PurchasePrice = models.DecimalField(decimal_places=2, max_digits=9, help_text='Price to purchase/replace the item.')
	Value = models.DecimalField(decimal_places=2, max_digits=9, help_text='Current value of the item')
	DateAcquired = models.DateField(help_text='Date item was acquired.')
	Status = models.CharField(max_length=50, help_text='Current Status of the item.')
	Warranty = models.DecimalField(decimal_places=3, max_digits=5, help_text='Manufacturer Warranty Period')
	#Metadata
	class Meta:
		ordering = ['Manufacturer', 'Model']
	def __str__(self):
	#	"""String for representing the Model object."""
		return f'{self.Manufacturer}, {self.Model}'