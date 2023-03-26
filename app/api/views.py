from core.api.base import APIResponse
from core.api.errors import Errors
from core.services.hashes import generate_unique_hash
from .stores import ImageStore


class Image:

    async def on_post(self, request, response):
        form = await request.get_media()
        async for part in form:
            if part.name == "image":
                image_id = generate_unique_hash()
                request_data = await part.stream.read()
                try:
                    response_data = await ImageStore().save(image_id, request_data)
                except:
                    raise Errors.DownloadError
                await APIResponse.Success(response_data).response(response)
            else:
                raise Errors.SomeError
