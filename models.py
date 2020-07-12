from django.db import models

category_choice=(
    ('IT','IT'),
('Electronics','Mobile'),
('Beauty','Lipstick'),
	('Wooden','Wooden'),
	('crockery','crockery'),
	('cloth','cloth'),

)

# Create your models here.
class Stock(models.Model):
	category = models.CharField(max_length=50, blank=True, null=True,choices=category_choice)
	item_name = models.CharField(max_length=50, blank=True, null=True)
	quantity = models.IntegerField(default='0', blank=True, null=True)
	issue_to=models.CharField(max_length=50)
	issue_quantity=models.IntegerField(default='0', blank=True, null=True)
	received_quantity = models.IntegerField(default='0', blank=True, null=True)
	receive_by = models.CharField(max_length=50, blank=True, null=True)
	reorder_level = models.IntegerField(default='0', blank=True, null=True)
	timestamp=models.DateTimeField(auto_now_add=True,auto_now=False)
	last_updated=models.DateTimeField(auto_now=True)

def __str__(self):
		return self.item_name