from typing import Any

import numpy as np
from ninja import Router

from recommender.PCA_KMeans import get_cluster
from recommender.baseline import get_match_score, get_top_3_field
from recommender.schema import MatchResultSchema, MatchError
from survey.models import Survey

recommender_router = Router()


def get_data_array(user_object):
    """
    Get survey data and weight in two numpy arrays
    :param user_object: Object instance from Survey model
    :return: data and weight in two numpy arrays
    """
    user_data = [user_object.getup_time, user_object.bed_time, user_object.social, user_object.academic,
                 user_object.bring_people, user_object.animal, user_object.instrument, user_object.cleaning,
                 user_object.cook, user_object.share, user_object.smoke, user_object.alcohol]
    user_data_weight = [user_object.getup_time_w, user_object.bed_time_w, user_object.social_w, user_object.academic_w,
                        user_object.bring_people_w, user_object.animal_w, user_object.instrument_w,
                        user_object.cleaning_w, user_object.cook_w, user_object.share_w, user_object.smoke_w,
                        user_object.alcohol_w]
    return np.array(user_data), np.array(user_data_weight)


def get_data_array_with_id(user_object):
    """
    Get survey data and weight in two numpy arrays with user_id as the 1st element in data array
    :param user_object: Object instance from Survey model
    :return: data and weight in two numpy arrays with user_id as the 1st element in data array
    """
    user_data = [user_object.user_id, user_object.getup_time, user_object.bed_time, user_object.social,
                 user_object.academic, user_object.bring_people, user_object.animal, user_object.instrument,
                 user_object.cleaning, user_object.cook, user_object.share, user_object.smoke, user_object.alcohol]
    user_data_weight = [user_object.getup_time_w, user_object.bed_time_w, user_object.social_w, user_object.academic_w,
                        user_object.bring_people_w, user_object.animal_w, user_object.instrument_w,
                        user_object.cleaning_w, user_object.cook_w, user_object.share_w, user_object.smoke_w,
                        user_object.alcohol_w]
    return np.array(user_data), np.array(user_data_weight)


def format_match_result(match_result_list: list[dict[str, Any]]) -> dict[str, list[Any]]:
    """
    Sort match result in descending order according to match score and provide dict matched with the output schema.
    :param match_result_list: list of dicts containing match result for each pair of matching
    :return: dict of 5 list match with the format of the output schema.
    """
    match_result_list.sort(key=lambda x: x["match_score"])
    output = {
        "user_id_list": [match_result["user_id"] for match_result in match_result_list],
        "match_score_list": [match_result["match_score"] for match_result in match_result_list],
        "first_match_field_list": [match_result["first_match_field"] for match_result in match_result_list],
        "second_match_field_list": [match_result["second_match_field"] for match_result in match_result_list],
        "third_match_field_list": [match_result["third_match_field"] for match_result in match_result_list],
    }
    return output


@recommender_router.get("/retrieve-match-result-base/{user_id}", response={200: MatchResultSchema, 403: MatchError})
def retrieve_match_result_base(request, user_id: int):
    current_user_survey = Survey.objects.get(user_id=user_id)  # get object of current user survey
    other_user_survey_query = Survey.objects.exclude(user_id=user_id)  # get queryset of objects of other users survey
    other_user_survey_list = list(other_user_survey_query)  # convert queryset to list

    # get data and weight of the current user in numpy array
    current_user_data, current_user_weight = get_data_array(current_user_survey)
    match_result_list = []
    for other_user_survey in other_user_survey_list:
        # get data and weight of the other user in numpy array
        other_user_data, other_user_weight = get_data_array(other_user_survey)
        match_score_base = get_match_score(current_user_data, current_user_weight, other_user_data,
                                           other_user_weight)  # calculate match score with baseline
        top_3_field = get_top_3_field(current_user_data, other_user_data)
        match_result_list.append({
            "user_id": other_user_survey.user_id,
            "match_score": match_score_base,
            "first_match_field": top_3_field[0],
            "second_match_field": top_3_field[1],
            "third_match_field": top_3_field[2]
        })
    #  sort in descending order based on match score
    output = format_match_result(match_result_list)
    return output


@recommender_router.get("/retrieve-match-result-cluster/{user_id}", response={200: MatchResultSchema, 403: MatchError})
def retrieve_match_result_cluster(request, user_id: int):
    current_user_survey = Survey.objects.get(user_id=user_id)  # get object of current user survey
    # get data and weight of the current user in numpy array
    current_user_data, current_user_weight = get_data_array(current_user_survey)

    all_user_survey = Survey.objects.all()  # get all object of user survey in queryset
    all_user_survey_list = list(all_user_survey)  # convert queryset to list
    all_user_data_list = []
    all_user_weight_list = []
    for survey_obj in all_user_survey_list:
        user_data, user_data_weight = get_data_array_with_id(survey_obj)
        all_user_data_list.append(user_data)
        all_user_weight_list.append(user_data_weight)
    match_score_list, cluster_index_list = get_cluster(all_user_data_list, all_user_weight_list, user_id)
    match_result_list = []

    # get list of user data that is within the same cluster of the current user without including current user
    # all_user_data_list[index] is the numpy array of the user data
    for index in cluster_index_list:
        if all_user_data_list[index][0] != user_id:
            top_3_field = get_top_3_field(current_user_data, np.delete(all_user_data_list[index], 0))
            match_result_list.append({
                "user_id": all_user_data_list[index][0],
                "match_score": match_score_list[index],
                "first_match_field": top_3_field[0],
                "second_match_field": top_3_field[1],
                "third_match_field": top_3_field[2]
            })
    output = format_match_result(match_result_list)
    return output



