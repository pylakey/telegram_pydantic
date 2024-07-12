from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputMediaPoll(BaseModel):
    """
    types.InputMediaPoll
    ID: 0xf94e5f1
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputMediaPoll', 'InputMediaPoll'] = pydantic.Field(
        'types.InputMediaPoll',
        alias='_'
    )

    poll: "base.Poll"
    correct_answers: typing.Optional[list[Bytes]] = None
    solution: typing.Optional[str] = None
    solution_entities: typing.Optional[list["base.MessageEntity"]] = None
