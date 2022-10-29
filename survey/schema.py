from ninja import Schema, ModelSchema
from survey.models import BasicInfo, Survey


class BasicInfoSchema(ModelSchema):
    class Config:
        model = BasicInfo
        model_fields = ["user_id", "user_name", "email", "password", "school_year", "rent", "move_in_date",
                        "number_of_room", "location"]


class BasicInfoUserNameSchema(Schema):
    user_name: int


class SurveySchema(ModelSchema):
    class Config:
        model = Survey
        model_fields = ["user_id", "getup_time", "getup_time_w", "bed_time", "bed_time_w", "social",
                        "social_w", "academic", "academic_w", "bring_people", "bring_people_w", "animal", "animal_w",
                        "instrument", "instrument_w", "cleaning", "cleaning_w", "cook", "cook_w", "share", "share_w",
                        "smoke", "smoke_w", "alcohol", "alcohol_w"]


class SurveyGetupTimeSchema(Schema):
    getup_time: int


class SurveyGetupTimeWSchema(Schema):
    getup_time_w: int


class SurveyBedTimeSchema(Schema):
    bed_time: int


class SurveyBedTimeWSchema(Schema):
    bed_time_w: int


class SurveySocialSchema(Schema):
    social: int


class SurveySocialWSchema(Schema):
    social_w: int


class SurveyAcademicSchema(Schema):
    academic: int


class SurveyAcademicWSchema(Schema):
    academic_w: int


class SurveyBringPeopleSchema(Schema):
    bring_people: int


class SurveyBringPeopleWSchema(Schema):
    bring_people_w: int


class BasicInfoSuccess(Schema):
    success: bool


class BasicInfoError(Schema):
    message: str


class SurveySuccess(Schema):
    success: bool


class SurveyError(Schema):
    message: str
