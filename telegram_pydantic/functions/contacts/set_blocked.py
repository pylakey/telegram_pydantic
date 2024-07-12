from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetBlocked(BaseModel):
    """
    functions.contacts.SetBlocked
    ID: 0x94c65c76
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.contacts.SetBlocked', 'SetBlocked'] = pydantic.Field(
        'functions.contacts.SetBlocked',
        alias='_'
    )

    id: list["base.InputPeer"]
    limit: int
    my_stories_from: typing.Optional[bool] = None
