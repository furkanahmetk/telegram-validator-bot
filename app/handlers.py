from urllib import response

# Function to start conversation and welcome the user
def start_command(update, context):
    update.message.reply_text('Hello! Welcome to Casper Validator Bot. Please type /signin '
    + 'to save your validator account information and start to use your bot')

# Function to get validator's public key
def get_public_key(update, context):
    update.message.reply_text('Type your Public Key: ')
    
# Function to handle user's messages
def handle_message(update, context):
    text = str(update.message.text).lower()
    response = responses(text)

    update.message.reply_text(response)
#Function that gives responses
def responses(input_text):
    user_message = str(input_text).lower()
    print("user entered a message: " + user_message)
    if user_message in ("how is my machine?","how is my validator?"):
        return "Your machine info: Will be updated"


def error(update, error):
    print(f"Update {update} caused error {error}")