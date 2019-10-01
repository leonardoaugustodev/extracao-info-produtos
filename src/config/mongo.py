import pymongo
import os


def conectaMongo():
    # Conecta no mongoDB #

    mongo = pymongo.MongoClient(os.environ.get('MONGO_URL'))

    return mongo
