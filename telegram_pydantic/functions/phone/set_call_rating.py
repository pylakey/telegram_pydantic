from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetCallRating(BaseModel):
    """
    functions.phone.SetCallRating
    ID: 0x59ead627
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.SetCallRating', 'SetCallRating'] = pydantic.Field(
        'functions.phone.SetCallRating',
        alias='_'
    )

    peer: "base.InputPhoneCall"
    rating: int
    comment: str
    user_initiative: typing.Optional[bool] = None
