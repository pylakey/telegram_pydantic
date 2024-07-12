from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetPollResults(BaseModel):
    """
    functions.messages.GetPollResults
    ID: 0x73bb643b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.GetPollResults', 'GetPollResults'] = pydantic.Field(
        'functions.messages.GetPollResults',
        alias='_'
    )

    peer: "base.InputPeer"
    msg_id: int
