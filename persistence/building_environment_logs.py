from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

load_dotenv()
url_string = os.getenv('MONGO_URL')


class BuildingEnvironment:
    def __init__(self, database=MongoClient(), database_name="aphrodite"):
        self.database = database
        self.database_name = database_name
        self.database_connection = self.database[self.database_name]
        self.collection_connection = self.database_connection["building_environments"]

        #   GET

    def get_environments(self):
        try:
            #   FETCH ALL DOCUMENTS AND RETURN AS LIST OF JSON OBJECTS
            environments = list(self.collection_connection.find())
            results = dumps(environments)
            return results
        except Exception as error:
            print(error)

    def get_environment_by_id(self, env_id):
        try:
            environment = self.collection_connection.find_one({"_id": ObjectId(env_id)})
            result = dumps(environment)
            return result
        except Exception as error:
            print(error)

    def get_environment_by_name(self, name):
        try:
            environments = self.collection_connection.find_one({"name": name})
            result = dumps(environments)
            return result
        except Exception as error:
            print(error)

    def get_environments_by_type(self, env_type):
        try:
            environments = self.collection_connection.find_one({"type": env_type})
            result = dumps(environments)
            return result
        except Exception as error:
            print(error)

        #   ADD

    def add_environment(self, environment):
        try:
            _id = self.collection_connection.insert_one(environment).inserted_id
            environment["_id"] = _id
            return environment
        except Exception as error:
            print(error)

        #   REMOVE

    def delete_environment(self, env_id):
        try:
            self.collection_connection.delete_one({'_id': ObjectId(env_id)})
            return "Deleted"
        except Exception as error:
            print(error)

    #   UPDATE

    def update_environment(self, environment):
        try:
            filter_values = {'_id': ObjectId(environment['_id'])}
            new_values = {"$set": environment}
            self.collection_connection.update_one(filter_values, new_values)
            return "Update Complete"
        except Exception as error:
            print(error)
