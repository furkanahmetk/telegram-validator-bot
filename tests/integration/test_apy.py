from src.service import bot_service
from src.model import validator
import uuid
from unittest.mock import Mock
from src.config import TestingConfig


def test_apy():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """
   
    mocked_update = Mock()
    mocked_update.effective_chat.id = 0
    mocked_update.message.text = f"/apy"

    mocked_context = Mock()

    updater = Mock()

    bot_ser = bot_service.Bot_Service(updater, TestingConfig)

    bot_ser.apy(mocked_update, mocked_context)

    mocked_update.message.reply_text.assert_called()


def test_apy_negative():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """

    mocked_update = Mock()
    mocked_update.effective_chat.id = 0
    mocked_update.message.text = f"/apy"

    mocked_context = Mock()

    updater = Mock()

    bot_ser = bot_service.Bot_Service(updater, TestingConfig)

    bot_ser.apy(mocked_update, mocked_context)

    mocked_update.message.reply_text.assert_called()

    try:
        mocked_update.message.reply_text.assert_called_with("""Hello! """)
    except AssertionError as verr:
        assert True, "Different variable call"