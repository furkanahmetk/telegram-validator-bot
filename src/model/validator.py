from distutils.log import error
from src.factory.validation import Validation
from src.factory.database import Database

"""
Wraps the data for database operations and overall usage. Validator keeps the data of validators in the network and it makes sure that 
validator data saved by the system correctly. It also defines which information of the validators will be saved to system
"""
class Validator(object):
    def __init__(self):
        self.validator = Validation()
        self.collection_name = 'validators'

        self.fields = {
            "_id": "string",
            "public_key": "string",
            "is_active": "bool",
            "fee": "float",
            "total_stake": "float",
            "delegators_number": "float",
            "performance": "float",
            "list_of_user_id_for_alarm": ["string"],
            "list_of_user_id_for_update": ["string"],
            "created": "datetime",
            "updated": "datetime"
        }

        self.create_required_fields = ["public_key", "is_active", "fee", "delegators_number", 
                                       "total_stake","list_of_user_id_for_alarm","list_of_user_id_for_update","performance"]

        # Fields optional for CREATE
        self.create_optional_fields = [
            "_id", "created", "updated"]

        # Fields required for UPDATE
        self.update_required_fields =  ["public_key", "is_active", "fee", "delegators_number", 
                                       "total_stake","list_of_user_id_for_alarm","list_of_user_id_for_update","performance"]

        # Fields optional for UPDATE
        self.update_optional_fields = [
            "_id", "created", "updated"]
    
    def convert_to_message(self,validator):
        return f"public Key: {validator['public_key']}\n fee:{validator['fee']}\n total stake:{validator['total_stake']}\n performance:{validator['performance']}\n status:{validator['is_active']}\n delegators count: {validator['delegators_number']}"

    def create(self, validator):
        # Validator will throw error if invalid
        self.validator.validate(
            validator, self.fields, self.create_required_fields, self.create_optional_fields)
        res = Database.insert(validator, self.collection_name)
        return "Inserted Id " + res

    def create_many(self, validator_list):
        for i in range(len(validator_list)):
            try:
                self.validator.validate(
                    validator_list[i], self.fields, self.create_required_fields, self.create_optional_fields)
            except Exception as e:
                print(e)

        return Database.insert_many(validator_list, self.collection_name)

    def find(self, validator):  # find all
        return Database.find(validator, self.collection_name)

    def find_by_id(self, id):
        return Database.find_by_id(id, self.collection_name)

    def update(self, id, validator):
        self.validator.validate(
            validator, self.fields, self.update_required_fields, self.update_optional_fields)
        return Database.update(id, validator, self.collection_name)

    def update_many(self, validator_list):
        for i in range(len(validator_list)):
            try:
                self.validator.validate(
                    validator_list[i], self.fields,  self.update_required_fields, self.update_optional_fields)
            except Exception as e:
                print(e)
        return Database.update_many(validator_list, self.collection_name)

    def delete(self, id):
        return Database.delete(id, self.collection_name)

    def find_one_by_public_key(self, public_key):
        validator_object_list = self.find({'public_key': public_key})

        if len(validator_object_list) == 0:
            return 'NONE'
        return validator_object_list[0]
