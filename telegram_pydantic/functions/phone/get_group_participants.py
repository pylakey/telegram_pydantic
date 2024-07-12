from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetGroupParticipants(BaseModel):
    """
    functions.phone.GetGroupParticipants
    ID: 0xc558d8ab
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.phone.GetGroupParticipants', 'GetGroupParticipants'] = pydantic.Field(
        'functions.phone.GetGroupParticipants',
        alias='_'
    )

    call: "base.InputGroupCall"
    ids: list["base.InputPeer"]
    sources: list[int]
    offset: str
    limit: int
