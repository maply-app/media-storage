import hashlib
import datetime
import os


def generate_unique_hash():
    now = datetime.datetime.now()
    h = hashlib.sha1(
        os.urandom(32)
        + "".join(str(now).split()).encode("utf-8")
        + os.urandom(32)
    ).hexdigest()
    return h


def generate_sha1_hash_by_value(value) -> str:
    return hashlib.sha1(str(value).encode('utf-8')).hexdigest()