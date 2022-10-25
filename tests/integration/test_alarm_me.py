from src.service import bot_service
from src.model import validator
import uuid
from unittest.mock import Mock
from src.config import TestingConfig


def test_alarm_me():
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
    user_id = str(uuid.uuid4())
    mocked_update.effective_chat.id =  user_id 
    mocked_update.message.text = f"/alarm {public_key}"

    mocked_context = Mock()

    updater = Mock()

    bot_ser = bot_service.Bot_Service(updater, TestingConfig)

    bot_ser.alarm_me(mocked_update, mocked_context)
    update_validator = validate.find_one_by_public_key(public_key)
    assert user_id in update_validator['list_of_user_id_for_alarm']


def test_update_me_negative():
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
    mocked_update.message.text = f"/alarm {public_key}"

    mocked_context = Mock()

    updater = Mock()

    bot_ser = bot_service.Bot_Service(updater, TestingConfig)

    bot_ser.alarm_me(mocked_update, mocked_context)

    update_validator = validate.find_one_by_public_key(public_key)
    assert not update_validator  == 'NONE'