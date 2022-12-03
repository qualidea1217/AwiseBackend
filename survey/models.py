from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


# Create your models here.

class BasicInfo(models.Model):
    # account basic info
    user_id = models.IntegerField(primary_key=True)
    user_name = models.TextField()
    email = models.TextField()
    password = models.TextField()
    gender = models.TextField()

    # student personal info
    school_year = models.IntegerField()

    # property info
    rent = models.IntegerField()
    move_in_date = models.TextField()  # models.DateField()
    number_of_room = models.IntegerField()
    location = models.TextField()


class ProfilePicture(models.Model):
    basic_info = models.OneToOneField(BasicInfo, on_delete=models.PROTECT, related_name="profile_picture", primary_key=True)
    profile_picture = models.ImageField(upload_to="profile_picture/")


class Survey(models.Model):
    user_id = models.IntegerField(primary_key=True)
    # basic_info = models.OneToOneField(BasicInfo, on_delete=models.CASCADE, primary_key=True)
    # habits and personality
    getup_time = models.IntegerField()
    getup_time_w = models.IntegerField()
    bed_time = models.IntegerField()
    bed_time_w = models.IntegerField()
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
        ])  # 'clean' is a keyword, don't use it as val name
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
