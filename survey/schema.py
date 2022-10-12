from datetime import datetime
from ninja import Schema


class SurveySchema(Schema):
    user_id: int
    user_name: str
    year: int
    rent: int
    move_in_date: str
    num_of_rm: int
    location: str
    social: int
    academic: int
    getup_time: int
    bed_time: int
    bring_people: int
    animal: int
    instrument: int
    clean: int
    cook: int
    share: int
    smoke: int
    alcohol: int

class UserBasicInfoSchema(Schema):
    is_authenticated: bool
    user_id: str
    user_name: str
    year: int
    email: str
    move_in_date: str
    num_of_rm: int
    location: str


class UserHabitSchema(Schema):
    getup_time: str
    bed_time: str
    bring_people: int
    animal: int
    instrument: int
    clean: int
    cook: int
    share: int
    smoke: int
    alcohol: int


class UserPersonalitySchema(Schema):
    academic: int
    introvert_extrovert: int


class Error(Schema):
    message: str
