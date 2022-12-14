# Generated by Django 4.1.1 on 2022-11-26 19:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("survey", "0003_alter_survey_bed_time_alter_survey_getup_time"),
    ]

    operations = [
        migrations.RemoveField(model_name="basicinfo", name="profile_picture",),
        migrations.CreateModel(
            name="ProfilePicture",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("profile_picture", models.ImageField(upload_to="profile_picture/")),
                (
                    "basic_info",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="profile_picture",
                        to="survey.basicinfo",
                    ),
                ),
            ],
        ),
    ]
