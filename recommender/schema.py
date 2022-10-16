from ninja import Schema


class Error(Schema):
    message: str


class MatchResult(Schema):
    match_user_info: list
    match_score: list[int]
    match_user_email: list[str]

