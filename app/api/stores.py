import io
import aiofiles
import PIL.Image
import config
import asyncio
from core.services.hashes import generate_sha1_hash_by_value
from .db import Image


class ImageStore:

    def load_from_bytes(self, data):
        return PIL.Image.open(io.BytesIO(data))

    def convert(self, image):
        rgb_image = image.convert("RGB")
        converted = io.BytesIO()
        rgb_image.save(converted, config.PIL_IMAGE_CONVERT_TYPE)
        return converted.getvalue()

    async def save(self, image_id: str, data: bytes) -> dict:
        loop = asyncio.get_running_loop()
        image = await loop.run_in_executor(None, self.load_from_bytes, data)

        # поиск дубликатов изображения
        image_hash = await loop.run_in_executor(None, generate_sha1_hash_by_value, data)
        status, image_id = Image.check_and_create(image_id=image_id, image_hash=image_hash)
        if not status:
            converted = await loop.run_in_executor(None, self.convert, image)
            path_to_save = "{}{}.{}".format(config.IMAGES_FULL_PATH, image_id, config.IMAGE_EXTENSION)
            async with aiofiles.open(path_to_save, "wb") as output:
                await output.write(converted)

        return {
            "image_id": str(image_id),
            "image": "{}.{}".format(image_id, config.IMAGE_EXTENSION),
        }
