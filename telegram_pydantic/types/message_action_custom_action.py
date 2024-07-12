from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionCustomAction(BaseModel):
    """
    types.MessageActionCustomAction
    ID: 0xfae69f56
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionCustomAction', 'MessageActionCustomAction'] = pydantic.Field(
        'types.MessageActionCustomAction',
        alias='_'
    )

    message: str
