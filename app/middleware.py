from core.api.errors import Errors
import config
import jwt
import asyncio


class UserJWT:
    async def process_request_async(self, request, response):
        header = request.headers.get("authorization")
        if not header:
            raise Errors.Unauthorized
        headerParts = header.split(" ")

        if len(headerParts) != 2 or headerParts[0] != "Bearer" or len(headerParts[1]) == 0:
            raise Errors.Unauthorized

        try:
            await asyncio.to_thread(
                jwt.decode,
                headerParts[1],
                bytes(config.SIGNING_KEY, encoding="utf8"),
                algorithms=["HS256"]
            )
        except:
            raise Errors.Unauthorized
