import numpy as np
from django.shortcuts import get_object_or_404

from survey.models import Survey
from recommender.baseline import get_match_score


class MatchResult:
    other_user_id: int
    similarity: float

    def __init__(self, main_user_id, other_user_id):
        self.other_user_id = other_user_id

        main_user = get_object_or_404(Survey, user_id=main_user_id)  # main user object
        other_user = get_object_or_404(Survey, user_id=main_user_id)  # other user object
        main_user_data = []
        other_user_data = []
        main_user_data.append(main_user.academic)
        other_user_data.append(other_user.academic)
        # TODO: append all fields that are going to use in calculating similarity

        self.similarity = get_match_score(np.array(main_user_data), np.ones(len(main_user_data)),
                                          np.array(other_user_data), np.ones(len(other_user_data)))



