from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

load_dotenv()
url_string = os.getenv('MONGO_URL')


class HumanoidCharacterLogs:
    def __init__(self, database=MongoClient(), database_name="aphrodite"):
        self.database = database
        self.database_name = database_name
        self.database_connection = self.database[self.database_name]
        self.collection_connection = self.database_connection["characters"]

        #   GET

    def get_characters(self):
        try:
            #   FETCH ALL DOCUMENTS AND RETURN AS LIST OF JSON OBJECTS
            characters = list(self.collection_connection.find())
            results = dumps(characters)
            return results
        except Exception as error:
            print(error)

    def get_character_by_id(self, character_id):
        try:
            character = self.collection_connection.find_one({"_id": ObjectId(character_id)})
            result = dumps(character)
            return result
        except Exception as error:
            print(error)

    def get_character_by_name(self, name):
        try:
            character = self.collection_connection.find_one({"name": name})
            result = dumps(character)
            return result
        except Exception as error:
            print(error)

    def get_characters_by_story(self, story):
        try:
            characters = self.collection_connection.find_one({"story": story})
            result = dumps(characters)
            return result
        except Exception as error:
            print(error)

        #   ADD

    def add_character(self, character):
        try:
            _id = self.collection_connection.insert_one(character).inserted_id
            character["_id"] = _id
            return character
        except Exception as error:
            print(error)

        #   REMOVE

    def delete_character(self, character_id):
        try:
            self.collection_connection.delete_one({'_id': ObjectId(character_id)})
            return "Deleted"
        except Exception as error:
            print(error)

    #   UPDATE

    def update_character(self, character):
        try:
            filter_values = {'_id': ObjectId(character['_id'])}
            new_values = {"$set": character}
            self.collection_connection.update_one(filter_values, new_values)
            return "Update Complete"
        except Exception as error:
            print(error)
