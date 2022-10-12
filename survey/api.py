from ninja import NinjaAPI

from survey.models import Survey
from survey.schema import SurveySchema, Error

api = NinjaAPI()


@api.post("/create-survey")
def create_survey(request, payload: SurveySchema):
    new_survey = Survey.objects.create(**payload.dict())
    return {"user_id": new_survey.id}


@api.get("/retrieve-survey/{user_id}", response={200: SurveySchema, 404: Error})
def retrieve_survey(request, user_id: int):
    return get_survey_or_404(user_id)


@api.get("/all-user-survey")
def get_all_survey(request):
    return Survey.objects.all()


@api.put("/update-survey/{user_id}")
def update_survey(request, user_id: int, payload: SurveySchema):
    survey = get_survey_or_404(user_id)
    for attr, value in payload.dict().items():
        setattr(survey, attr, value)
    survey.save()
    return {"success": True}


@api.delete("/delete-survey/{user_id}")
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
