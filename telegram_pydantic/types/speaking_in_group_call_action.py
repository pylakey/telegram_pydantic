from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SpeakingInGroupCallAction(BaseModel):
    """
    types.SpeakingInGroupCallAction
    ID: 0xd92c2285
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SpeakingInGroupCallAction', 'SpeakingInGroupCallAction'] = pydantic.Field(
        'types.SpeakingInGroupCallAction',
        alias='_'
    )

