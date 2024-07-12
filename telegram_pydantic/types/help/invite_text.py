from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InviteText(BaseModel):
    """
    types.help.InviteText
    ID: 0x18cb9f78
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.InviteText', 'InviteText'] = pydantic.Field(
        'types.help.InviteText',
        alias='_'
    )

    message: str
