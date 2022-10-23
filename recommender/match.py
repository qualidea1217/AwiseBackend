import numpy as np

from survey.models import Survey
from recommender.schema import MatchResult, Error
from recommender.baseline import get_match_score
from survey.api import get_survey_or_404


class MatchResult:
    other_user_id: int
    similarity: float

    def __init__(self, main_user_id, other_user_id):
        self.other_user_id = other_user_id

        main_user = get_survey_or_404(main_user_id)  # object
        other_user = get_survey_or_404(other_user_id)  # object
        if main_user == 404:
            raise Exception(f"Main user (user id: {main_user_id}) does not exist.")
        elif other_user == 404:
            raise Exception(f"Other user (user id: {other_user_id}) does not exist.")
        main_user_data = []
        other_user_data = []
        main_user_data.append(main_user.academic)
        other_user_data.append(other_user.academic)
        # TODO: append all fields that are going to use in calculating similarity

        self.similarity = get_match_score(np.array(main_user_data), np.ones(len(main_user_data)),
                                          np.array(other_user_data), np.ones(len(other_user_data)))



