from django.db import models

# Create your models here.

class DaysData(models.Model):
	title = models.DateTimeField(auto_now_add = True, auto_now = False)

	def __str__(self):
		return 


class TickerData(models.Model):
	name = models.CharField(max_length=20)
	symbol = models.CharField(max_length=10)
	opening_price = models.FloatField()
	intrinsic_value = models.FloatField()
	fcfy = models.FloatField()
	pe_ratio = models.FloatField()
	peg_ratio = models.FloatField()
	market_cap = models.FloatField()
	day = models.ForeignKey(DaysData)