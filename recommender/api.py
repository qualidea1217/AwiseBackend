from ninja import NinjaAPI
import numpy as np

from recommender.models import Survey
from recommender.schema import MatchResult, Error
from recommender.algorithm import get_match_score

api = NinjaAPI()


@api.get("/retrieve-match-result/{user_id}", response={200: MatchResult, 404: Error})
def retrieve_base_match_result(request, user_id: int):
    current_user_info = Survey.objects.get(user_id)
    user_list = []  # TODO: retrieve all user id to get all user
    user_info_list = [Survey.objects.get(user) for user in user_list if user != user_id]  # exclude current user itself
    # TODO: convert user_info to a ndarray, compute match score, store in a list with same sequence
    match_score_list = [get_match_score(current_user_info, np.array([1] * len(current_user_info)),
                                        user_info, np.array([1] * len(current_user_info)))
                        for user_info in user_info_list]  # TODO: add weight array
    # TODO: return the result

