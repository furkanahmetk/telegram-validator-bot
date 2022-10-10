from curses import reset_shell_mode
from email import message
from urllib import response
import requests
import json
import logging
import telegram
validator = str #global variable for holding the user's validator ID(pubKey)
# Function to start conversation and welcome the user
def start_command(update, context):

    welcomeMessage = """Hello! Welcome to Casper Validator Bot.
Please enter your request as below:\n
He
/totaldelegators <validator's public key>
/totalstake <validator's public key>
/fee <validator's public key>
/start_timer <validator's public key>
    """
    update.message.reply_text(welcomeMessage)
# Function to get validator's status


#common function to make get request to backend and return the 'message' from result
def requester(method,validator):
    URL = "http://38.242.242.73:5555/"+method+"?pubKey=" + validator
    return requests.get(URL).json()["message"]

#start's job_queue(cron job). User needs to message '/start_timer <pubKey>'
def start_timer(update, context):
    global validator
    text = update.message.text
    validator = text.split()[1]
    user_id = update.effective_chat.id
    context.bot.send_message(chat_id=user_id, text='Timer Started!')
    context.job_queue.run_repeating(callback=send_timer_message, interval = 10, context=user_id)


# function to send timer's message to user.
def send_timer_message(context):
    global validator
    user_id = context.job.context
    # bugcamp search
    bugcamp_data_curr = requester("state",validator)

    # send message and update
    context.bot.send_message(chat_id=user_id, text=bugcamp_data_curr, parse_mode=telegram.ParseMode.MARKDOWN)


def status(update, context):
    text = update.message.text
    validator = text.split()[1]
    print(validator)
    res = requester("state",validator)
    update.message.reply_text(res)

def totaldelegators(update, context):
    text = update.message.text
    validator = text.split()[1]
    res = requester("totalDelegators",validator)
    update.message.reply_text(res)

def totalstake(update, context):
    text = update.message.text
    validator = text.split()[1]
    res = requester("totalStake",validator)
    update.message.reply_text(res)

def fee(update, context):
    update.message.reply_text('Fee')

#THESE METHODS ARE FOR USER'S PERSONALIZED MESSAGES
# Function to handle user's messages
def handle_message(update, context):
    text = str(update.message.text).lower()
    print(f'User {update.message.chat.username} says {text}')
    response = responses(text)

    update.message.reply_text(response)

#Function that gives responses
def responses(input_text):
    user_message = str(input_text).lower()
    print("responses")
    print("user entered a message: " + user_message)
    if user_message in ("how is my machine?","how is my validator?"):
        return "Your machine info: Will be updated"
    


def error(update, error):
    print("error: ",error.error)
    update.message.reply_text("Error: "+error.error.message)