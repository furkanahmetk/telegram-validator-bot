from src.service.bot_service import Bot_Service
from src.service import data
from src.model import validator
from enum import Enum


 
class Alarm_Change(Enum):
    FEE_INCREASE = 'FEE INCREASE'
    FEE_DECREASE = 'FEE DECREASE'
    DELEGATOR_NUMBER = 'DELEGATOR NUMBER CHANGE'
    TOTAL_STAKE = 'TOTAL STAKE CHANGE'
    ACTIVE = 'ACTIVATION'
    NOT_ACTIVE = 'DEACTIVATION'
    NONE = 'no change happened'


"""
Defines repeated jobs of the system. It calls, controls and saves the data flow to the system. It seperates the data already in the system with the new data.
It either inserts or updates the data
"""
class Repeated_Task():
    
    def __init__(self,updater,config):
            self.data = data.Data(config)
            self.validator = validator.Validator()
            self.updater = updater
            self.bot_service = Bot_Service(self.updater,config)

    def data_cron(self):
        validators_in_db = self.validator.find({})
        validators_in_db_public_keys = [item['public_key'] for item in validators_in_db]
        validators_in_db_dict = {item['public_key']: item for item in validators_in_db}


        #Get validator data from data object
        new_validator_values = self.data.get_validator_list(validators_in_db_public_keys)
        new_validator_values_dict = {item['public_key']: item for item in new_validator_values}

        
        self.alarm_users(validators_in_db_dict,new_validator_values_dict)
        self.update_users(validators_in_db_dict,new_validator_values_dict)
        self.update_data(validators_in_db_dict,new_validator_values_dict)

    def alarm_users(self,db_validators,new_validators):
        for key in new_validators:
            if key in db_validators:
                change = self.alarm_change(db_validators[key],new_validators[key])
                if change != Alarm_Change.NONE:
                    item = new_validators[key]
                    self.bot_service.update_user(f"ALARM {change.value} \n {self.validator.convert_to_message(item)}",db_validators[key]['list_of_user_id_for_alarm'])
                 

    def alarm_change(self,old_item,new_item):

        if (old_item['is_active'] != new_item['is_active']):
            if new_item['is_active']:
                return Alarm_Change.ACTIVE
            else:
                return Alarm_Change.NOT_ACTIVE
        if (old_item['fee'] != new_item['fee']):
            if new_item['fee'] > old_item['fee']:
                return Alarm_Change.FEE_INCREASE
            else: 
                return Alarm_Change.FEE_DECREASE
        if (old_item['delegators_number'] != new_item['delegators_number']):
            return Alarm_Change.DELEGATOR_NUMBER
        if (old_item['total_stake'] != new_item['total_stake']):
            return Alarm_Change.TOTAL_STAKE
        return Alarm_Change.NONE
        

    def update_users(self,db_validators,new_validators):
        for key in new_validators:
            if key in db_validators:
                item = new_validators[key]
                self.bot_service.update_user(f"Update for {self.validator.convert_to_message(item)}",db_validators[key]['list_of_user_id_for_update'])
                    

    def update_data(self,db_validators,new_validators):
        new_validator_list = []
        for key in new_validators:
            if key in db_validators:
                new_item = new_validators[key]
                item = db_validators[key]
                item['fee'] = new_item['fee']
                item['is_active'] = new_item['is_active']
                item['delegators_number'] = new_item['delegators_number']
                item['total_stake'] = new_item['total_stake']
                new_validator_list.append(item)
        self.validator.update_many(new_validator_list)