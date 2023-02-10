from mongoengine import *


class Image(Document):
    image_id = StringField(max_length=100, required=True)
    image_hash = StringField(max_length=100, required=True)

    @classmethod
    def check_and_create(cls, image_id, image_hash) -> tuple:
        images = cls.objects(image_hash=image_hash)
        if images.count() > 0:
            return (True, images.first().image_id)
        image = cls(image_id=image_id, image_hash=image_hash)
        image.save()
        return (False, image_id)