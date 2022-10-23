from django.db import models

# Create your models here.

class Survey_1(models.Model):
	# basic info
	user_id = models.AutoField(primary_key=True)
	user_name = models.TextField()
	y = models.IntegerField()
	
	rent = models.IntegerField()
	move_in_date = models.IntegerField() # models.DateField()
	num_of_rm = models.IntegerField()
	location = models.TextField()
	
	# habits
	getup_time = models.IntegerField()
	bed_time = models.IntegerField()
	
	# email and password
	email = models.TextField()
	password = models.TextField()
   

class Survey_2(models.Model):
	# personality
	survey_1 = models.OneToOneField(Survey_1, on_delete = models.CASCADE, primary_key = True)
	social = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	social_w = models.IntegerField()
	academic = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	academic_w = models.IntegerField()
	bring_people = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	bring_people_w = models.IntegerField()
	animal = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	animal_w = models.IntegerField()
	instrument = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	instrument_w = models.IntegerField()
	cleaning = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ]) # 'clean' is a keyword, don't use it as val name
	cleaning_w = models.IntegerField()
	cook = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	cook_w = models.IntegerField()
	share = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	share_w = models.IntegerField()
	smoke = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	smoke_w = models.IntegerField()
	alcohol = models.IntegerField(
		validators=[
            MaxValueValidator(10),
            MinValueValidator(1)
        ])
	alcohol_w = models.IntegerField()
	
