from core.api.base import APIResponse
from core.api.errors import Errors
from core.services.hashes import generate_unique_hash
from .stores import ImageStore


class Image:

    async def on_post(self, request, response):

        # try:
        #     input_file = request.get_param("file")

        #     # Read file as binary
        #     request_data = input_file.file.read()
        # except Exception as e:
        #     print(e)
        try:
            request_data = await request.stream.read()
            image_id = generate_unique_hash()
            try:
                response_data = await ImageStore().save(image_id, request_data)
            except Exception as e:
                print(f"Exception #2 –> {e}")
                raise Errors.DownloadError
        except Exception as e:
            print(f"Exception #1 –> {e}")
        await APIResponse.Success(response_data).response(response)
