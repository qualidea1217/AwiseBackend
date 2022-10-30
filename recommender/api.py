from ninja import Router
import numpy as np

from survey.models import Survey
from recommender.schema import MatchResultSchema, MatchError
from recommender.baseline import get_match_score

recommender_router = Router()


def get_data_array(user_object):
    user_data = [user_object.getup_time, user_object.bed_time, user_object.social, user_object.academic,
                 user_object.bring_people, user_object.animal, user_object.instrument, user_object.cleaning,
                 user_object.cook, user_object.share, user_object.smoke, user_object.alcohol]
    user_data_weight = [user_object.getup_time_w, user_object.bed_time_w, user_object.social_w, user_object.academic_w,
                        user_object.bring_people_w, user_object.animal_w, user_object.instrument_w,
                        user_object.cleaning_w, user_object.cook_w, user_object.share_w, user_object.smoke_w,
                        user_object.alcohol_w]
    return np.array(user_data), np.array(user_data_weight)


@recommender_router.get("/retrieve-match-result-base/{user_id}", response={200: MatchResultSchema, 403: MatchError})
def retrieve_match_result(request, user_id: int):
    current_user_survey = Survey.objects.get(user_id)  # get object of current user survey
    other_user_survey_query = Survey.objects.exclude(user_id=user_id)  # get queryset of objects of other users survey
    other_user_survey_list = list(other_user_survey_query)  # convert queryset to list

    # get data and weight of the current user in numpy array
    current_user_data, current_user_data_weight = get_data_array(current_user_survey)
    match_result_list = []
    for other_user_survey in other_user_survey_list:
        # get data and weight of the other user in numpy array
        other_user_data, other_user_data_weight = get_data_array(other_user_survey)
        match_score_base = get_match_score(current_user_data, current_user_data_weight, other_user_data,
                                           other_user_data_weight)  # calculate match score with baseline
        match_result_list.append({"user_id": other_user_survey.user_id, "match_score": match_score_base})
    #  sort in descending order based on match score
    match_result_list.sort(key=lambda x: x["match_score"], reverse=True)
    return match_result_list
