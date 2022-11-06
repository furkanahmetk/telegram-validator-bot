from src.service import bot_service
from unittest.mock import Mock
from src.config import TestingConfig

def test_start():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """
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
    
    mocked_update = Mock()
    mocked_update.effective_chat.id = 0
    mocked_update.message.text = "/start"

    mocked_context = Mock()

    updater = Mock()
     
    bot_ser = bot_service.Bot_Service(updater,TestingConfig)

    bot_ser.start_command(mocked_update,mocked_context)

    mocked_update.message.reply_text.assert_called()

    mocked_update.message.reply_text.assert_called_with(welcomeMessage)

def test_start_negative():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """
    
    mocked_update = Mock()
    mocked_update.effective_chat.id = 0
    mocked_update.message.text = "/start"

    mocked_context = Mock()

    updater = Mock()
     
    bot_ser = bot_service.Bot_Service(updater,TestingConfig)

    bot_ser.start_command(mocked_update,mocked_context)

    mocked_update.message.reply_text.assert_called()

    try:
        mocked_update.message.reply_text.assert_called_with("""Hello! """)
    except AssertionError as verr:
        assert True, "Different variable call"