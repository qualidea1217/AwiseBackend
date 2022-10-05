from ninja import NinjaAPI, Schema

api = NinjaAPI()


class UserBasicInfoSchema(Schema):
    is_authenticated: bool
    user_id: str
    user_name: str
    year: int
    email: str
    move_in_date: str
    num_of_rm: int
    location: str


class UserHabitSchema(Schema):
    getup_time: str
    bed_time: str
    bring_people: int
    animal: int
    instrument: int
    clean: int
    cook: int
    share: int
    smoke: int
    alcohol: int


class UserPersonalitySchema(Schema):
    academic: int
    introvert_extrovert: int


class Error(Schema):
    message: str


@api.get("/me", response={200: UserBasicInfoSchema, 403: Error})
def me(request):
    if not request.user.is_authenticated:
        return 403, {"message": "Please sign in first"}
    return request.user


class HelloSchema(Schema):
    name: str = "world"


@api.post("/hello")
def hello(request, data: HelloSchema):
    return f"Hello {data.name}"


@api.get("/math/{a}and{b}")
def math(request, a: int, b: int):
    return {"add": a + b, "multiply": a * b}
