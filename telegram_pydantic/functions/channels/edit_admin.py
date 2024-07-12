from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class EditAdmin(BaseModel):
    """
    functions.channels.EditAdmin
    ID: 0xd33c8902
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.channels.EditAdmin', 'EditAdmin'] = pydantic.Field(
        'functions.channels.EditAdmin',
        alias='_'
    )

    channel: "base.InputChannel"
    user_id: "base.InputUser"
    admin_rights: "base.ChatAdminRights"
    rank: str
