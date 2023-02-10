from core.api.errors import Errors
import config
import jwt


class UserJWT:

    async def process_request(self, request, response):
        header = request.headers.get("Authorization")
        if not header:
            raise Errors.Unauthorized
        headerParts = header.split(" ")

        if len(headerParts) != 2 or headerParts[0] != "Bearer" or len(headerParts[1]) == 0:
            raise Errors.Unauthorized

        try:
            jwt.decode(headerParts[1], config.SIGNING_KEY, algorithms=["HS256"])
        except:
            raise Errors.Unauthorized

