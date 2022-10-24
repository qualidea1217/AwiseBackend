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


class BasicInfoError(Schema):
    message: str


class SurveyError(Schema):
    message: str
