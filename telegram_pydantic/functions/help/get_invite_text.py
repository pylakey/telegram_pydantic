from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetInviteText(BaseModel):
    """
    functions.help.GetInviteText
    ID: 0x4d392343
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.GetInviteText', 'GetInviteText'] = pydantic.Field(
        'functions.help.GetInviteText',
        alias='_'
    )

