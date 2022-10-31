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



# RU for survey social
@survey_router.get("/retrieve-survey-social/{user_id}", response={200: SurveySocialSchema, 403: SurveyError})
def retrieve_survey_social(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.social


@survey_router.put("/update-survey-social/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_social(request, user_id: int, payload: SurveySocialSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.social = payload.social
    survey.save()
    return 200, {"success": True}


# RU for survey social weight
@survey_router.get("/retrieve-survey-social-w/{user_id}", response={200: SurveySocialWSchema, 403: SurveyError})
def retrieve_survey_social_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.social_w


@survey_router.put("/update-survey-social-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_social_w(request, user_id: int, payload: SurveySocialWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.social_w = payload.social_w
    survey.save()
    return 200, {"success": True}



# RU for survey social
@survey_router.get("/retrieve-survey-academic/{user_id}", response={200: SurveyAcademicSchema, 403: SurveyError})
def retrieve_survey_academic(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.academic


@survey_router.put("/update-survey-academic/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_academic(request, user_id: int, payload: SurveyAcademicSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.academic = payload.academic
    survey.save()
    return 200, {"success": True}


# RU for survey academic weight
@survey_router.get("/retrieve-survey-academic-w/{user_id}", response={200: SurveyAcademicWSchema, 403: SurveyError})
def retrieve_survey_academic_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.academic_w


@survey_router.put("/update-survey-academic-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_academic_w(request, user_id: int, payload: SurveyAcademicWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.academic_w = payload.academic_w
    survey.save()
    return 200, {"success": True}


# RU for survey bring_people
@survey_router.get("/retrieve-survey-bring-people/{user_id}", response={200: SurveyBringPeopleSchema, 403: SurveyError})
def retrieve_survey_bring_people(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.bring_people


@survey_router.put("/update-survey-bring-people/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_bring_people(request, user_id: int, payload: SurveyBringPeopleSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.bring_people = payload.bring_people
    survey.save()
    return 200, {"success": True}


# RU for survey bring_people weight
@survey_router.get("/retrieve-survey-bring-people-w/{user_id}", response={200: SurveyBringPeopleWSchema, 403: SurveyError})
def retrieve_survey_bring_people_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.bring_people_w


@survey_router.put("/update-survey-bring-people-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_bring_people_w(request, user_id: int, payload: SurveyBringPeopleWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.bring_people_w = payload.bring_people_w
    survey.save()
    return 200, {"success": True}


# RU for survey animal
@survey_router.get("/retrieve-survey-animal/{user_id}", response={200: SurveyAnimalSchema, 403: SurveyError})
def retrieve_survey_animal(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.animal


@survey_router.put("/update-survey-animal/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_animal(request, user_id: int, payload: SurveyAnimalSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.animal = payload.animal
    survey.save()
    return 200, {"success": True}


# RU for survey animal weight
@survey_router.get("/retrieve-survey-animal-w/{user_id}", response={200: SurveyAnimalWSchema, 403: SurveyError})
def retrieve_survey_animal_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.animal_w


@survey_router.put("/update-survey-animal-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_animal_w(request, user_id: int, payload: SurveyAnimalWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.animal_w = payload.animal_w
    survey.save()
    return 200, {"success": True}


# RU for survey instrument
@survey_router.get("/retrieve-survey-instrument/{user_id}", response={200: SurveyInstrumentSchema, 403: SurveyError})
def retrieve_survey_instrument(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.instrument


@survey_router.put("/update-survey-instrument/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_instrument(request, user_id: int, payload: SurveyInstrumentSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.instrument = payload.instrument
    survey.save()
    return 200, {"success": True}


# RU for survey instrument weight
@survey_router.get("/retrieve-survey-instrument-w/{user_id}", response={200: SurveyInstrumentWSchema, 403: SurveyError})
def retrieve_survey_instrument_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.instrument_w


@survey_router.put("/update-survey-instrument-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_instrument_w(request, user_id: int, payload: SurveyInstrumentWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.instrument_w = payload.instrument_w
    survey.save()
    return 200, {"success": True}


# RU for survey cleaning
@survey_router.get("/retrieve-survey-cleaning/{user_id}", response={200: SurveyCleaningSchema, 403: SurveyError})
def retrieve_survey_cleaning(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.cleaning


@survey_router.put("/update-survey-cleaning/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_cleaning(request, user_id: int, payload: SurveyCleaningSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.cleaning = payload.cleaning
    survey.save()
    return 200, {"success": True}


# RU for survey cleaning weight
@survey_router.get("/retrieve-survey-cleaning-w/{user_id}", response={200: SurveyCleaningWSchema, 403: SurveyError})
def retrieve_survey_cleaning_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.cleaning_w


@survey_router.put("/update-survey-cleaning-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_cleaning_w(request, user_id: int, payload: SurveyCleaningWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.cleaning_w = payload.cleaning_w
    survey.save()
    return 200, {"success": True}


# RU for survey cook
@survey_router.get("/retrieve-survey-cook/{user_id}", response={200: SurveyCookSchema, 403: SurveyError})
def retrieve_survey_cook(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.cook


@survey_router.put("/update-survey-cook/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_cook(request, user_id: int, payload: SurveyCookSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.cook = payload.cook
    survey.save()
    return 200, {"success": True}


# RU for survey cleaning weight
@survey_router.get("/retrieve-survey-cook-w/{user_id}", response={200: SurveyCookWSchema, 403: SurveyError})
def retrieve_survey_cook_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.cook_w


@survey_router.put("/update-survey-cook-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_cook_w(request, user_id: int, payload: SurveyCookWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.cook_w = payload.cook_w
    survey.save()
    return 200, {"success": True}




# RU for survey share
@survey_router.get("/retrieve-survey-share/{user_id}", response={200: SurveyShareSchema, 403: SurveyError})
def retrieve_survey_share(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.share


@survey_router.put("/update-survey-share/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_share(request, user_id: int, payload: SurveyShareSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.share = payload.share
    survey.save()
    return 200, {"success": True}


# RU for survey share weight
@survey_router.get("/retrieve-survey-share-w/{user_id}", response={200: SurveyShareWSchema, 403: SurveyError})
def retrieve_survey_share_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.share_w


@survey_router.put("/update-survey-share-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_share_w(request, user_id: int, payload: SurveyShareWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.share_w = payload.share_w
    survey.save()
    return 200, {"success": True}


# RU for survey smoke
@survey_router.get("/retrieve-survey-smoke/{user_id}", response={200: SurveySmokeSchema, 403: SurveyError})
def retrieve_survey_smoke(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.smoke


@survey_router.put("/update-survey-smoke/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_smoke(request, user_id: int, payload: SurveySmokeSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.smoke = payload.smoke
    survey.save()
    return 200, {"success": True}


# RU for survey smoke weight
@survey_router.get("/retrieve-survey-smoke-w/{user_id}", response={200: SurveySmokeWSchema, 403: SurveyError})
def retrieve_survey_smoke_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.smoke_w


@survey_router.put("/update-survey-smoke-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_smoke_w(request, user_id: int, payload: SurveySmokeWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.smoke_w = payload.smoke_w
    survey.save()
    return 200, {"success": True}


# RU for survey alcohol
@survey_router.get("/retrieve-survey-alcohol/{user_id}", response={200: SurveyAlcoholSchema, 403: SurveyError})
def retrieve_survey_alcohol(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.alcohol


@survey_router.put("/update-survey-alcohol/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_alcohol(request, user_id: int, payload: SurveyAlcoholSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.alcohol = payload.alcohol
    survey.save()
    return 200, {"success": True}


# RU for survey alcohol weight
@survey_router.get("/retrieve-survey-alcohol-w/{user_id}", response={200: SurveyAlcoholWSchema, 403: SurveyError})
def retrieve_survey_alcohol_w(request, user_id: int):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    return survey.alcohol_w


@survey_router.put("/update-survey-alcohol-w/{user_id}", response={200: SurveySuccess, 403: SurveyError})
def update_survey_alcohol_w(request, user_id: int, payload: SurveyAlcoholWSchema):
    try:
        survey = Survey.objects.get(user_id=user_id)
    except Survey.DoesNotExist:
        return 403, {"message": "Survey Does Not Exist."}
    survey.alcohol_w = payload.alcohol_w
    survey.save()
    return 200, {"success": True}


