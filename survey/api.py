from ninja import Router

from recommender.schema import Error
from survey.models import Survey_1, Survey_2
from survey.schema import SurveySchema

survey_router = Router()


api = NinjaAPI()


class Survey1Schema(Schema):
    is_authenticated: bool
    user_id: str
    user_name: str
    email: str
    y: int
    rent: int
    move_in_date: int
    num_of_rm: int
    location: str
    getup_time: int
    bed_time: int
    
    


class Survey2Schema(Schema):
    social: int
    academic: int
    bring_people: int
    animal: int
    instrument: int
    clean: int
    cook: int
    share: int
    smoke: int
    alcohol: int



@api.post("/survey1")
def create_survey1(request):
    Survey_1.objects.create()
    return {}

@api.post("/survey2")
def create_survey2(request):
    Survey_2.objects.create()
    return {'success': True}


class Q1(Schema):
    user_name: str

@api.put("/q1/{user_id}")
def q1(request, user_id: int, usr_name: Q1):
    user = get_object_or_404(Survey_1, id=user_id)
    user,user_name = Q1.user_name
    return {'success': True}

"""

@survey_router.post("/create-survey")
def create_survey(request, payload: SurveySchema):
    new_survey = Survey.objects.create(**payload.dict())
    return {"user_id": new_survey.id}


@survey_router.get("/retrieve-survey/{user_id}", response={200: SurveySchema, 404: Error})
def retrieve_survey(request, user_id: int):
    return get_survey_or_404(user_id)


@survey_router.get("/all-user-survey")
def get_all_survey(request):
    return Survey.objects.all()


@survey_router.put("/update-survey/{user_id}")
def update_survey(request, user_id: int, payload: SurveySchema):
    survey = get_survey_or_404(user_id)
    for attr, value in payload.dict().items():
        setattr(survey, attr, value)
    survey.save()
    return {"success": True}


@survey_router.delete("/delete-survey/{user_id}")
def delete_survey(request, user_id: int):
    survey = get_survey_or_404(user_id)
    survey.delete()
    return {"success": True}


def get_survey_or_404(user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 404
    return survey
"""
