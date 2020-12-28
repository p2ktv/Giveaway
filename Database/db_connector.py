import pymongo
from pymongo import MongoClient


def db_connection(db_pass):
    try:
        return MongoClient(db_pass).general
    except Exception as db_connection_error:
        print("Error while connecting to DB: {}".format(db_connection_error))