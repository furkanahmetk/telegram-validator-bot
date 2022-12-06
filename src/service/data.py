import requests

"""
Onject that speciliazed for daflow to the system. It retrieves data from given address.
"""
class Data(object):

    def __init__(self,config):
        self.base_url= config.BASE_URL
    
    def get_validator_list(self,validators_list):
        PAYLOAD = {'publicKeys':validators_list}
        r = requests.post(url = self.base_url+'getAllValidatorValues', json = PAYLOAD)
        if r.status_code == 200:
            data = r.json()
            return data
        else:
            return 'NONE'
    
    def get_validator_status(self,validator_public_key):
        PARAMS = {'pubKey':validator_public_key}
        r = requests.get(url = self.base_url+'/state', params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            message = data['message']
            return message
        else:
            return 'NONE'
    def get_validator_delegationRate(self,validator_public_key):
        PARAMS = {'pubKey':validator_public_key}
        r = requests.get(url = self.base_url+'/delegationRate', params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            message = data['message']
            return message
        else:
            return 'NONE'
    def get_validator_totalStake(self,validator_public_key):
        PARAMS = {'pubKey':validator_public_key}
        r = requests.get(url = self.base_url+'/totalStake', params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            message = data['message']
            return message
        else:
            return 'NONE'

    def get_validator_performance(self,validator_public_key):
        PARAMS = {'pubKey':validator_public_key}
        r = requests.get(url = self.base_url+'/performance', params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            message = data['message']
            return message
        else:
            return 'NONE'

    def get_apy(self):
        r = requests.get(url = self.base_url+'/apy')
        if r.status_code == 200:
            data = r.json()
            message = data['message']
            return message
        else:
            return 'NONE'

    def get_validator_totalDelegators(self,validator_public_key):
        PARAMS = {'pubKey':validator_public_key}
        r = requests.get(url = self.base_url+'/totalDelegators', params = PARAMS)
        if r.status_code == 200:
            data = r.json()
            message = data['message']
            return message
        else:
            return 'NONE'

    def get_value_from_message(self,message):
        return message.split(": ")[1]
