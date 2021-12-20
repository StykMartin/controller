from typing import Any, Generic, Type, TypeVar

from pydantic import BaseModel
from simplexml import dumps, loads  # type: ignore
from starlette.requests import Request
from starlette.responses import Response

T = TypeVar("T", bound=BaseModel)


class XMLResponse(Response):
    media_type = "application/xml"

    def render(self, content: Any) -> bytes:
        return dumps({"response": content}).encode("utf-8")


class XmlBody(Generic[T]):
    def __init__(self, model_class: Type[T]):
        self.model_class = model_class

    async def __call__(self, request: Request) -> T:
        # the following check is unnecessary if always using xml,
        # but enables the use of json too
        if request.headers.get("Content-Type") == "application/xml":
            body = await request.body()
            dict_data = loads(body)
        else:
            dict_data = await request.json()
        return self.model_class.parse_obj(dict_data)
