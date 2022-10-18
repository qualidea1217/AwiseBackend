from ninja import Router

from survey.models import Survey
from survey.schema import SurveySchema, Error

import numpy as np
from recommender.models import Survey
from recommender.schema import MatchResult, Error
from recommender.algorithm import get_match_score

survey_router = Router()


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
