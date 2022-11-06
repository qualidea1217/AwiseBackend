from ninja import NinjaAPI
from survey.api import survey_router
from recommender.api import recommender_router

api = NinjaAPI()
api.add_router("/survey/", survey_router)
api.add_router("/recommender/", recommender_router)

