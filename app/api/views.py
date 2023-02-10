from core.api.base import APIResponse
from core.api.errors import Errors
from core.services.hashes import generate_unique_hash
from .stores import ImageStore


class Image:

    async def on_post(self, request, response):
        request_data = await request.stream.read()
        image_id = generate_unique_hash()
        try:
            response_data = await ImageStore().save(image_id, request_data)
        except Exception:
            raise Errors.DownloadError
        await APIResponse.Success(response_data).response(response)
