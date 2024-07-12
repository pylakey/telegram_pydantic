from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessBotRecipients(BaseModel):
    """
    types.InputBusinessBotRecipients
    ID: 0xc4e5921e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessBotRecipients', 'InputBusinessBotRecipients'] = pydantic.Field(
        'types.InputBusinessBotRecipients',
        alias='_'
    )

    existing_chats: typing.Optional[bool] = None
    new_chats: typing.Optional[bool] = None
    contacts: typing.Optional[bool] = None
    non_contacts: typing.Optional[bool] = None
    exclude_selected: typing.Optional[bool] = None
    users: typing.Optional[list["base.InputUser"]] = None
    exclude_users: typing.Optional[list["base.InputUser"]] = None
