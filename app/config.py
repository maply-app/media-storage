import os

# JWT
SIGNING_KEY = os.getenv("SIGNING_KEY")

# Изображения
IMAGES_FULL_PATH = "/usr/src/app/images/"
IMAGE_EXTENSION = "webp"
PIL_IMAGE_CONVERT_TYPE = "WebP"

# База
MONGO_USERNAME = os.getenv("MONGO_INITDB_ROOT_USERNAME")
MONGO_PASSWORD = os.getenv("MONGO_INITDB_ROOT_PASSWORD")
MONGO_DATABASE = os.getenv("MONGO_INITDB_DATABASE")
MONGO_HOSTNAME = os.getenv("MONGO_HOST")