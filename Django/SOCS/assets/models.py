import uuid
from django.db import models



# Create your models here.

class Asset(models.Model):
	#Fields
	ITEQUIP = 'ITEQUIP'
	MACHINERY = 'MACHINERY'
	TOOLS = 'TOOLS'
	ELECTRICALEQUIP = 'ELECTRICALEQUIP'
	FURNITURE = 'FURNITURE'
	DIGITAL = 'DIGITAL'
	UNCATEGORIZED = 'UNCATEGORIZED'


	ASSET_TYPE_CHOICES = [
		(ITEQUIP,'IT Equipment'),
		(MACHINERY,'Machinery'),
		(TOOLS, 'Tools'),
		(ELECTRICALEQUIP,'Electrical Equipment'),
		(FURNITURE, 'Furniture'),
		(DIGITAL, 'Digital'),
		(UNCATEGORIZED, 'Uncategorized'),
	]

	AssetID = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	AssetType = models.CharField(max_length=50, help_text='Type of Asset',choices=ASSET_TYPE_CHOICES, default = UNCATEGORIZED,)
	Name = models.CharField(max_length=50, help_text='Item Name')
	Manufacturer = models.CharField(max_length=50, help_text='Manufacturer Name', blank=True)
	Model = models.CharField(max_length=50, help_text='Manufacturer Model', blank=True)
	Location = models.CharField(max_length=50, help_text='Location Stored/Kept in space')
	Owner = models.CharField(max_length=50, help_text='Owner')
	Description = models.CharField(max_length=200, help_text='Item Description')
	Notes = models.CharField(max_length=200, help_text='Item Notes - Include Serial # where applicable.', blank=True)
	PurchasePrice = models.DecimalField(decimal_places=2, max_digits=9, help_text='Price to purchase/replace the item.')
	Value = models.DecimalField(decimal_places=2, max_digits=9, help_text='Current value of the item')
	DateAcquired = models.DateField(help_text='Date item was acquired.')
	Status = models.CharField(max_length=50, help_text='Current Status of the item.')
	Warranty = models.DecimalField(decimal_places=3, max_digits=5, help_text='Manufacturer Warranty Period')
	InspectionPeriod = models.DecimalField(decimal_places=3, max_digits=5, help_text='Period between inspections where applicable in months.',blank=True)
	NextInspection = models.DateField(help_text='Next inspection date',blank=True)
	DateRetired = models.DateField(help_text='Date of retirement, destruction or sale etc.', blank=True)
	
	#Metadata
	class Meta:
		ordering = ['Manufacturer', 'Model']
	def __str__(self):
	#	"""String for representing the Model object."""
		return f'{self.Manufacturer}, {self.Model}'