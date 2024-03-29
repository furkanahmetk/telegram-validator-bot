from src.service.data import Data
from src.model.validator import Validator
validator = str #global variable for holding the user's validator ID(pubKey)
# Function to start conversation and welcome the user
empty_pubkey_error = "Please type a validator public key!"
class Bot_Service():
    def __init__(self,updater,config):
            self.data = Data(config)
            self.validator = Validator()
            self.updater=updater

    def start_command(self,update,context):
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        else:
            update.message.reply_text("Hello👋 Welcome to Casper Validator Bot.")
            welcomeMessage = """Please enter your request as below:
    /status <validator's public key>
    /totaldelegators <validator's public key>
    /totalstake <validator's public key>
    /apy
    /performance <validator's public key>
    /fee <validator's public key>
    /update <validator's public key>
    /alarm <validator's public key>
    /forget <validator's public key>
            """
            update.message.reply_text(welcomeMessage)

    def status(self,update, context):

        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
                
        else:
            validator = self.get_validator_key(update)
            asked_validator = self.validator.find_one_by_public_key(validator)        
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if asked_validator == "NONE":
                res = self.data.get_validator_status(validator)
            else:
                if asked_validator['is_active']:
                    res = "active"
                else:
                    res = "not active"
            if res == 'NONE':
                self.no_validator(update,context)
                return
            res_validator = validator[:5:] + "..."+ validator[-5::]
            res_message = "Status of "+res_validator+": "+res.upper()
            update.message.reply_text(res_message)

    def apy(self,update, context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")        
        
        else:
            res = self.data.get_apy()
            if res == 'NONE':
                self.no_apy(update,context)
                return
            res_message="Annual Percentage Yield: "+str(res)
            update.message.reply_text(res_message)

    def performance(self,update, context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator = self.get_validator_key(update)
            asked_validator = self.validator.find_one_by_public_key(validator)
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if asked_validator == "NONE":
                res = self.data.get_validator_performance(validator)
            else:
                res = asked_validator['performance']
            if res == 'NONE':
                self.no_validator(update,context)
                return
            res_validator = validator[:5:] + "..."+ validator[-5::]
            res_message = "Performance of "+str(res_validator)+": "+str(round(float(res),ndigits=1))+"%"
            update.message.reply_text(res_message)

    def total_delegators(self,update, context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator = self.get_validator_key(update)
            asked_validator = self.validator.find_one_by_public_key(validator)
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if asked_validator == "NONE":
                res = self.data.get_validator_totalDelegators(validator)
            else:
                res = asked_validator['delegators_number']
            if res == 'NONE':
                self.no_validator(update,context)
                return
            res_validator = validator[:5:] + "..."+ validator[-5::]
            res_message = "The number of total delegators of "+str(res_validator)+": "+str(res)
            update.message.reply_text(res_message)

    def total_stake(self,update, context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator = self.get_validator_key(update)
            asked_validator = self.validator.find_one_by_public_key(validator)
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if asked_validator == "NONE":
                res = self.data.get_validator_totalStake(validator)
            else:
                res = asked_validator['total_stake']
            if res == 'NONE':
                self.no_validator(update,context)
                return
            res_validator = validator[:5:] + "..."+ validator[-5::]
            res = int(res) / (10**9)
            res_message = "The number of total stake of "+str(res_validator)+": "+str(round(res,ndigits=2))
            update.message.reply_text(res_message)
    
    def fee(self,update, context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator = self.get_validator_key(update)
            asked_validator = self.validator.find_one_by_public_key(validator)
            
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if asked_validator == "NONE":
                res = self.data.get_validator_delegationRate(validator)
            else:
                res = asked_validator['fee']
            
            
            res_validator = validator[:5:] + "..."+ validator[-5::]
            res_message = "The fee of "+str(res_validator)+": "+str(res)+"%"
            update.message.reply_text(res_message)
            return


    def update_me(self,update,context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator_key = self.get_validator_key(update)
            validator_in_db = self.validator.find_one_by_public_key(validator_key)
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if validator_in_db == 'NONE':
                update_list = [validator_key]
                validator_new = self.data.get_validator_list(update_list)
                if validator_new == 'NONE' or len(validator_new) == 0:
                    self.no_validator(update,context)
                    return
                else:
                    validator_new = validator_new[0]
                    user_id = update.effective_chat.id
                    self.validator.create({
                        'public_key':validator_new['public_key'],
                        'is_active':validator_new['is_active'],
                        'fee':validator_new['fee'],
                        'total_stake':validator_new['total_stake'],
                        'performance':validator_new['performance'],
                        'delegators_number':validator_new['delegators_number'],
                        'list_of_user_id_for_alarm':[],
                        'list_of_user_id_for_update':[user_id]
                    })
                    validator_in_db = validator_new
            else:
                user_id = update.effective_chat.id
                validator_in_db['list_of_user_id_for_update'].append(user_id)
                self.validator.update(validator_in_db['_id'],{
                        'public_key':validator_in_db['public_key'],
                        'is_active':validator_in_db['is_active'],
                        'fee':validator_in_db['fee'],
                        'total_stake':validator_in_db['total_stake'],
                        'delegators_number':validator_in_db['delegators_number'],
                        'performance':validator_in_db['performance'],
                        'list_of_user_id_for_alarm':validator_in_db['list_of_user_id_for_alarm'],
                        'list_of_user_id_for_update':validator_in_db['list_of_user_id_for_update']
                    })
            update.message.reply_text(self.validator.convert_to_message(validator_in_db))

    def forget_validator(self,update,context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator_key = self.get_validator_key(update)
            validator_in_db = self.validator.find_one_by_public_key(validator_key)
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if validator_in_db == 'NONE':
                self.no_validator(update,context)
                return
            else:
                user_id = update.effective_chat.id
                if user_id in validator_in_db['list_of_user_id_for_update']:
                    validator_in_db['list_of_user_id_for_update'].remove(user_id)
                if user_id in validator_in_db['list_of_user_id_for_alarm']:
                    validator_in_db['list_of_user_id_for_alarm'].remove(user_id)
                self.validator.update(validator_in_db['_id'],{
                    'public_key':validator_in_db['public_key'],
                    'is_active':validator_in_db['is_active'],
                    'fee':validator_in_db['fee'],
                    'total_stake':validator_in_db['total_stake'],
                    'performance':validator_in_db['performance'],
                    'delegators_number':validator_in_db['delegators_number'],
                    'list_of_user_id_for_alarm':validator_in_db['list_of_user_id_for_alarm'],
                    'list_of_user_id_for_update':validator_in_db['list_of_user_id_for_update']
                })
            update.message.reply_text('I forgot validator for you')
    
    def alarm_me(self,update,context):
        
        if update.message.chat.type == 'group' and context.bot.getChatMember(chat_id=update.message.chat_id, user_id=update.message.from_user.id).status not in ('administrator', 'creator') :
            context.bot.send_message(chat_id=update.effective_chat.id, text="Sorry, only group admins can query this bot.")
        
        else:        
            validator_key = self.get_validator_key(update)
            validator_in_db = self.validator.find_one_by_public_key(validator_key)
            if len(update.message.text.split()) != 2:
                update.message.reply_text(empty_pubkey_error)
                return
            if validator_in_db == 'NONE':
                update_list = [validator_key]
                validator_new = self.data.get_validator_list(update_list)
                if validator_new == 'NONE' or len(validator_new) == 0:
                    self.no_validator(update,context)
                    return
                else:
                    validator_new = validator_new[0]
                    user_id = update.effective_chat.id
                    self.validator.create({
                        'public_key':validator_new['public_key'],
                        'is_active':validator_new['is_active'],
                        'fee':validator_new['fee'],
                        'total_stake':validator_new['total_stake'],
                        'delegators_number':validator_new['delegators_number'],
                        'performance':validator_new['performance'],
                        'list_of_user_id_for_alarm':[user_id],
                        'list_of_user_id_for_update':[]
                    })
                    validator_in_db = validator_new
            else:
                user_id = update.effective_chat.id
                validator_in_db['list_of_user_id_for_alarm'].append(user_id)
                self.validator.update(validator_in_db['_id'],{
                        'public_key':validator_in_db['public_key'],
                        'is_active':validator_in_db['is_active'],
                        'fee':validator_in_db['fee'],
                        'total_stake':validator_in_db['total_stake'],
                        'delegators_number':validator_in_db['delegators_number'],
                        'performance':validator_in_db['performance'],
                        'list_of_user_id_for_alarm':validator_in_db['list_of_user_id_for_alarm'],
                        'list_of_user_id_for_update':validator_in_db['list_of_user_id_for_update']
                    })
            update.message.reply_text(self.validator.convert_to_message(validator_in_db))


    def no_validator(self,update,context):
        welcomeMessage = """Sorry we could not found validator with this public key."""
        update.message.reply_text(welcomeMessage)

    def no_apy(self,update,context):
        welcomeMessage = """Sorry we could not get apy from system"""
        update.message.reply_text(welcomeMessage)
    
    def get_apy_value(self,text):
        return text.split('apy:')[1]

    def update_user(self, message, user_id_list):
        for user_id in user_id_list:
            self.updater.bot.sendMessage(chat_id=user_id, text=message)
       

    def error(self,update, error):
        update.message.reply_text(f"Error: {error.error}")

    def get_validator_key(self,update):
        text = update.message.text
        if len(text.split()) != 2:
            return 
        return text.split()[1]

