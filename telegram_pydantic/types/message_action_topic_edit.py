from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MessageActionTopicEdit(BaseModel):
    """
    types.MessageActionTopicEdit
    ID: 0xc0944820
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MessageActionTopicEdit', 'MessageActionTopicEdit'] = pydantic.Field(
        'types.MessageActionTopicEdit',
        alias='_'
    )

    title: typing.Optional[str] = None
    icon_emoji_id: typing.Optional[int] = None
    closed: typing.Optional[bool] = None
    hidden: typing.Optional[bool] = None
