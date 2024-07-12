from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerEmpty(BaseModel):
    """
    types.InputPeerEmpty
    ID: 0x7f3b18ea
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerEmpty', 'InputPeerEmpty'] = pydantic.Field(
        'types.InputPeerEmpty',
        alias='_'
    )

