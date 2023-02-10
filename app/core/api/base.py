import falcon
from typing import Union
from core.api.errors import CustomException
import json


class APIResponse:

    data: Union[dict, list] = None
    error: CustomException = None

    def __init__(self, data: Union[dict, list] = None, error: CustomException = None):
        self.data = data
        self.error = error

    @classmethod
    def Success(cls, data: Union[dict, list] = None) -> "APIResponse":
        return cls(data=data)

    @classmethod
    def Error(cls, error: CustomException) -> "APIResponse":
        return cls(error=error)

    async def response(self, response) -> None:
        response_data = {}
        response_data["status"] = "success" if not self.error else "error"

        if self.data is not None:
            response_data["data"] = self.data

        if self.error:
            response_data["code"] = self.error.code
            response_data["message"] = self.error.message

        response.status = falcon.HTTP_200
        response.content_type = "application/json"
        response.text = json.dumps(response_data)