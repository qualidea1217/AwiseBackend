from django.db import models

# Create your models here.
class Survey(models.Model):
	# basic info
	user_id = models.IntegerField()
	user_name = models.TextField()
	year = models.IntegerField()
	rent = models.IntegerField()
	move_in_date = models.DateField()
	num_of_rm = models.IntegerField()
	location = models.TextField()
	# personality
	social = models.IntegerField()
	academic = models.IntegerField()
	# habits
	getup_time = models.IntegerField()
	bed_time = models.IntegerField()
	bring_people = models.IntegerField()
	animal = models.IntegerField()
	instrument = models.IntegerField()
	clean = models.IntegerField()
	cook = models.IntegerField()
	share = models.IntegerField()
	smoke = models.IntegerField()
	alcohol = models.IntegerField()
    


