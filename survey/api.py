from django.shortcuts import get_object_or_404
from ninja import Router

from survey.models import BasicInfo, Survey
from survey.schema import BasicInfoSchema, SurveySchema, BasicInfoError, SurveyError

survey_router = Router()


# CRUD for basic info as a whole
@survey_router.post("/create-basic-info")
def create_basic_info(request, payload: BasicInfoSchema):
    new_basic_info = BasicInfo.objects.create(**payload.dict())
    return {"user_id": new_basic_info.id}


@survey_router.get("/retrieve-basic-info/{user_id}", response={200: BasicInfoSchema, 404: BasicInfoError})
def retrieve_basic_info(request, user_id: int):
    basic_info = get_object_or_404(BasicInfo, user_id=user_id)
    return basic_info


@survey_router.put("/update-basic-info/{user_id}")
def update_basic_info(request, user_id: int, payload: BasicInfoSchema):
    basic_info = get_object_or_404(BasicInfo, user_id=user_id)
    for attr, value in payload.dict().items():
        setattr(basic_info, attr, value)
    basic_info.save()
    return {"success": True}


@survey_router.delete("/delete-basic-info/{user_id}")
def delete_basic_info(request, user_id: int):
    basic_info = get_object_or_404(BasicInfo, user_id=user_id)
    basic_info.delete()
    return {"success": True}


# CRUD for Survey as a whole
@survey_router.post("/create-survey")
def create_survey(request, payload: SurveySchema):
    new_survey = Survey.objects.create(**payload.dict())
    return {"user_id": new_survey.id}


@survey_router.get("/retrieve-survey/{user_id}", response={200: SurveySchema, 404: SurveyError})
def retrieve_survey(request, user_id: int):
    survey = get_object_or_404(Survey, user_id=user_id)
    return survey


@survey_router.put("/update-survey/{user_id}")
def update_survey(request, user_id: int, payload: SurveySchema):
    survey = get_object_or_404(Survey, user_id=user_id)
    for attr, value in payload.dict().items():
        setattr(survey, attr, value)
    survey.save()
    return {"success": True}


@survey_router.delete("/delete-survey/{user_id}")
def delete_survey(request, user_id: int):
    survey = get_object_or_404(Survey, user_id=user_id)
    survey.delete()
    return {"success": True}

