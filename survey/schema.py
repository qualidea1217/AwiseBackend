from ninja import Schema, ModelSchema
from survey.models import BasicInfo, ProfilePicture, Survey


class BasicInfoSchema(ModelSchema):
    class Config:
        model = BasicInfo
        model_fields = ["user_id", "user_name", "email", "password", "gender", "school_year", "rent",
                        "move_in_date", "number_of_room", "location"]


class BasicInfoUserNameSchema(Schema):
    user_name: str


class BasicInfoEmailSchema(Schema):
    email: str


class BasicInfoPasswordSchema(Schema):
    password: str


class BasicInfoGenderSchema(Schema):
    gender: str


class ProfilePictureSchema(Schema):
    profile_picture: str


class BasicInfoSchoolYearSchema(Schema):
    school_year: int


class BasicInfoRentSchema(Schema):
    rent: int


class BasicInfoMoveInDateSchema(Schema):
    move_in_date: str


class BasicInfoNumberOfRoomSchema(Schema):
    number_of_room: int


class BasicInfoLocationSchema(Schema):
    location: str


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


class SurveyAnimalSchema(Schema):
    animal: int


class SurveyAnimalWSchema(Schema):
    animal_w: int


class SurveyInstrumentSchema(Schema):
    instrument: int


class SurveyInstrumentWSchema(Schema):
    instrument_w: int


class SurveyCleaningSchema(Schema):
    cleaning: int


class SurveyCleaningWSchema(Schema):
    cleaning_w: int


class SurveyCookSchema(Schema):
    cook: int


class SurveyCookWSchema(Schema):
    cook_w: int


class SurveyShareSchema(Schema):
    share: int


class SurveyShareWSchema(Schema):
    share_w: int


class SurveySmokeSchema(Schema):
    smoke: int


class SurveySmokeWSchema(Schema):
    smoke_w: int


class SurveyAlcoholSchema(Schema):
    alcohol: int


class SurveyAlcoholWSchema(Schema):
    alcohol_w: int


class BasicInfoSuccess(Schema):
    success: bool


class BasicInfoError(Schema):
    message: str


class SurveySuccess(Schema):
    success: bool


class SurveyError(Schema):
    message: str
