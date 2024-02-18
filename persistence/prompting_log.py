#   THIS LOGS ALL PROMPT RESPONSES TO AND FROM THE CHOSEN NLP
#   [ KEY - VALUE PAIRS ] => [ KEYS : PROMPT, RESPONSE, TIMESTAMP,NLP]
#   LOCAL PERSISTENCE SOLUTION WITH A GOOGLE DRIVE BACKUP UTILIZING CSV AND JSON
from pymongo import MongoClient
from dotenv import load_dotenv
from bson.json_util import dumps
from bson.objectid import ObjectId
import os

load_dotenv()
url_string = os.getenv('MONGO_URL')


class PromptingLog:
    def __init__(self, database=MongoClient(), database_name="aphrodite"):
        self.database = database
        self.database_name = database_name
        self.database_connection = self.database[self.database_name]
        self.collection_connection = self.database_connection["prompts"]

    #   GET
    def get_prompts(self):
        try:
            #   FETCH ALL DOCUMENTS AND RETURN AS LIST OF JSON OBJECTS
            prompts = list(self.collection_connection.find())
            results = dumps(prompts)
            return results
        except Exception as error:
            print(error)

    def get_prompt_by_id(self, prompt_id):
        try:
            prompt = self.collection_connection.find_one({"_id": ObjectId(prompt_id)})
            result = dumps(prompt)
            return result
        except Exception as error:
            print(error)

    def get_prompt_by_timestamp(self, timestamp):
        try:
            prompts = self.collection_connection.find_one({"timestamp": timestamp})
            result = dumps(prompts)
            return result
        except Exception as error:
            print(error)

    #   ADD

    def add_prompt(self, prompt):
        try:
            _id = self.collection_connection.insert_one(prompt).inserted_id
            prompt["_id"] = _id
            return prompt
        except Exception as error:
            print(error)

    #   REMOVE
    def delete_prompt(self, prompt_id):
        try:
            self.collection_connection.delete_one({'_id': ObjectId(prompt_id)})
            return "Deleted"
        except Exception as error:
            print(error)
    #   UPDATE

