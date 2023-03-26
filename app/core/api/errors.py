from typing import Optional, Union


class CustomException(Exception):

    code: int
    message: str

    def __init__(self, code: Union[int, "CustomException"], message: Optional[str] = None):
        if isinstance(code, CustomException) and message is None:
            self.code = code.code
            self.message = code.message

        self.code = code
        self.message = message

    def __str__(self):
        return "{} — \"{}\"".format(self.code, self.message)


class Errors:
    SomeError = CustomException(1, "Some exception occurred")
    DownloadError = CustomException(3010, "Error when uploading a file")
    Unauthorized = CustomException(401, "Unauthorized")
    HttpResponseForbidden = CustomException(403, "Http response forbidden")
    HTTPMethodNotAllowed = CustomException(405, "Http method not allowed")
