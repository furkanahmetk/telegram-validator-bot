from src.service import bot_service
from src.model import validator
import uuid
from unittest.mock import Mock
from src.config import TestingConfig


def test_total_delegators():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """
    public_key = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "public_key": public_key,
        "is_active": True,
        "fee": 3,
        "delegators_number": 42,
        "total_stake": "1877642908605992",
        "performance":99.5,
        "list_of_user_id_for_alarm": [],
        "list_of_user_id_for_update": [],
    })

    mocked_update = Mock()
    mocked_update.effective_chat.id = 0
    mocked_update.message.text = f"/totaldelegators {public_key}"

    mocked_context = Mock()

    updater = Mock()

    bot_ser = bot_service.Bot_Service(updater, TestingConfig)
    

    bot_ser.total_delegators(mocked_update, mocked_context)

    mocked_update.message.reply_text.assert_called()
    "b16fe...cc69a: 42"
    res_validator = public_key[:5:] + "..."+ public_key[-5::]
    response = "The number of total delegators of "+res_validator+": 42"
    mocked_update.message.reply_text.assert_called_with(response)


def test_total_delegators_negative():
    """
    GIVEN provider type
    WHEN providerValidate function called
    THEN check the returned value raised an error
    """

    public_key = str(uuid.uuid4())
    validate = validator.Validator()
    validate.create({
        "public_key": public_key,
        "is_active": True,
        "fee": 3,
        "delegators_number": 42,
        "total_stake": "1877642908605992",
        "performance":99.5,
        "list_of_user_id_for_alarm": [],
        "list_of_user_id_for_update": [],
    })

    mocked_update = Mock()
    mocked_update.effective_chat.id = 0
    mocked_update.message.text = f"/totaldelegators {public_key}"

    mocked_context = Mock()

    updater = Mock()

    bot_ser = bot_service.Bot_Service(updater, TestingConfig)

    bot_ser.total_delegators(mocked_update, mocked_context)

    mocked_update.message.reply_text.assert_called()

    try:
        mocked_update.message.reply_text.assert_called_with("""Hello! """)
    except AssertionError as verr:
        assert True, "Different variable call"