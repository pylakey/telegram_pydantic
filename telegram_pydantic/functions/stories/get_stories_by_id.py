from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetStoriesByID(BaseModel):
    """
    functions.stories.GetStoriesByID
    ID: 0x5774ca74
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.stories.GetStoriesByID', 'GetStoriesByID'] = pydantic.Field(
        'functions.stories.GetStoriesByID',
        alias='_'
    )

    peer: "base.InputPeer"
    id: list[int]
