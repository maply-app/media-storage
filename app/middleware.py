from core.api.errors import Errors
import config
import jwt

class UserJWT:

    async def process_request(self, request, response):
        try:
            header = request.headers.get("Authorization")
            headerParts = header.split(" ")

            if len(headerParts) != 2 or headerParts[0] != "Bearer" or len(headerParts[1]) == 0:
                raise Errors.Unauthorized

            try:
                jwt.decode(headerParts[1], config.SIGNING_KEY, algorithms=["HS256"])
            except:
                raise Errors.Unauthorized
        except Exception as e:
            print(e)

