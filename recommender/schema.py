from ninja import Schema


class MatchError(Schema):
    message: str


class MatchResultSchema(Schema):
    user_id_list: list[int]
    user_email_list: list[str]
    match_score_list: list[float]
    first_match_field_list: list[list[str, float]]
    second_match_field_list: list[list[str, float]]
    third_match_field_list: list[list[str, float]]
