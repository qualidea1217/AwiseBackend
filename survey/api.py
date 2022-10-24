from django.shortcuts import get_object_or_404
from ninja import Router

from survey.schema import *
from survey.models import BasicInfo, Survey

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


# RU for basic info user name
@survey_router.post("/retrieve-basic-info-user-name/{user_id}", response={200: BasicInfoUserNameSchema, 404: BasicInfoError})
def retrieve_basic_info_user_id(request, user_id: int):
    basic_info_user_name = get_object_or_404(BasicInfo, user_id=user_id).user_name
    return basic_info_user_name


@survey_router.put("/update-basic-info-user-name/{user-id}")
def update_basic_info_user_id(request, user_id: int, payload: BasicInfoUserNameSchema):
    basic_info = get_object_or_404(BasicInfo, user_id=user_id)
    basic_info.user_name = payload.user_name
    basic_info.save()
    return {"success": True}


# RU for survey getup time
@survey_router.post("/retrieve-survey-getup-time/{user_id}", response={200: SurveyGetupTimeSchema, 404: SurveyError})
def retrieve_survey_getup_time(request, user_id: int):
    survey_user_getup_time = get_object_or_404(Survey, user_id=user_id).getup_time
    return survey_user_getup_time


@survey_router.put("/update-survey-getup-time/{user-id}")
def update_survey_getup_time(request, user_id: int, payload: SurveyGetupTimeSchema):
    survey = get_object_or_404(Survey, user_id=user_id)
    survey.getup_time = payload.getup_time
    survey.save()
    return {"success": True}

