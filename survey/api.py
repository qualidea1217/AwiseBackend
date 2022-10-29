from ninja import Router

from survey.schema import *

survey_router = Router()


# CRUD for basic info as a whole
@survey_router.post("/create-basic-info")
def create_basic_info(request, payload: BasicInfoSchema):
    new_basic_info = BasicInfo.objects.create(**payload.dict())
    return {"user_id": new_basic_info.id}


@survey_router.get("/retrieve-basic-info/{user_id}", response={200: BasicInfoSchema, 403: BasicInfoError})
def retrieve_basic_info(request, user_id: int):
    try:
        basic_info = BasicInfo.objects.get(user_id=user_id)
    except BasicInfo.DoesNotExist:
        return 403, {"message": "Basic Info Does Not Exist."}
    return basic_info


@survey_router.put("/update-basic-info/{user_id}", response={200: BasicInfoSuccess, 403: BasicInfoError})
def update_basic_info(request, user_id: int, payload: BasicInfoSchema):
    try:
        basic_info = BasicInfo.objects.get(user_id=user_id)
    except BasicInfo.DoesNotExist:
        return 403, {"message": "Basic Info Does Not Exist."}
    for attr, value in payload.dict().items():
        setattr(basic_info, attr, value)
    basic_info.save()
    return 200, {"success": True}


@survey_router.delete("/delete-basic-info/{user_id}", response={200: BasicInfoSuccess, 403: BasicInfoError})
def delete_basic_info(request, user_id: int):
    try:
        basic_info = BasicInfo.objects.get(user_id=user_id)
    except BasicInfo.DoesNotExist:
        return 403, {"message": "Basic Info Does Not Exist."}
    basic_info.delete()
    return 200, {"success": True}


# CRUD for Survey as a whole
@survey_router.post("/create-survey")
def create_survey(request, payload: SurveySchema):
    new_survey = Survey.objects.create(**payload.dict())
    return {"user_id": new_survey.id}


@survey_router.get("/retrieve-survey/{user_id}", response={200: SurveySchema, 403: SurveyError})
def retrieve_survey(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey


@survey_router.put("/update-survey/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey(request, user_id: int, payload: SurveySchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    for attr, value in payload.dict().items():
        setattr(survey, attr, value)
    survey.save()
    return 200, {"success": True}


@survey_router.delete("/delete-survey/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def delete_survey(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.delete()
    return 200, {"success": True}


# RU for basic info user name
@survey_router.get("/retrieve-basic-info-user-name/{user_id}", response={200: BasicInfoUserNameSchema, 403: BasicInfoError})
def retrieve_basic_info_user_name(request, user_id: int):
    try:
        basic_info = BasicInfo.objects.get(user_id=user_id)
    except BasicInfo.DoesNotExist:
        return 403, {"message": "Basic Info Does Not Exist."}
    return basic_info.user_name


@survey_router.put("/update-basic-info-user-name/{user_id}", response={200: BasicInfoSuccess, 403: BasicInfoError})
def update_basic_info_user_name(request, user_id: int, payload: BasicInfoUserNameSchema):
    try:
        basic_info = BasicInfo.objects.get(user_id=user_id)
    except BasicInfo.DoesNotExist:
        return 403, {"message": "Basic Info Does Not Exist."}
    basic_info.user_name = payload.user_name
    basic_info.save()
    return 200, {"success": True}


# RU for survey getup time
@survey_router.get("/retrieve-survey-getup-time/{user_id}", response={200: SurveyGetupTimeSchema, 403: SurveyError})
def retrieve_survey_getup_time(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.getup_time


@survey_router.put("/update-survey-getup-time/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_getup_time(request, user_id: int, payload: SurveyGetupTimeSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.getup_time = payload.getup_time
    survey.save()
    return 200, {"success": True}


# RU for survey getup time weight
@survey_router.get("/retrieve-survey-getup-time-w/{user_id}", response={200: SurveyGetupTimeWSchema, 403: SurveyError})
def retrieve_survey_getup_time_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.getup_time_w


@survey_router.put("/update-survey-getup-time-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_getup_time_w(request, user_id: int, payload: SurveyGetupTimeWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.getup_time_w = payload.getup_time_w
    survey.save()
    return 200, {"success": True}


# RU for survey bed time
@survey_router.get("/retrieve-survey-bed-time/{user_id}", response={200: SurveyBedTimeSchema, 403: SurveyError})
def retrieve_survey_bed_time(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.bed_time


@survey_router.put("/update-survey-bed-time/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_bed_time(request, user_id: int, payload: SurveyBedTimeSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.bed_time = payload.bed_time
    survey.save()
    return 200, {"success": True}


# RU for survey bed time weight
@survey_router.get("/retrieve-survey-bed-time-w/{user_id}", response={200: SurveyBedTimeWSchema, 403: SurveyError})
def retrieve_survey_bed_time_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.bed_time_w


@survey_router.put("/update-survey-bed-time-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_bed_time_w(request, user_id: int, payload: SurveyBedTimeWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.bed_time_w = payload.bed_time_w
    survey.save()
    return 200, {"success": True}

