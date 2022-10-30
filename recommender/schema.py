from ninja import Schema


class MatchError(Schema):
    message: str


class MatchResultSchema(Schema):
    match_result = list[dict]

