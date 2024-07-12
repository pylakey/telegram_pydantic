from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPeerSelf(BaseModel):
    """
    types.InputPeerSelf
    ID: 0x7da07ec9
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPeerSelf', 'InputPeerSelf'] = pydantic.Field(
        'types.InputPeerSelf',
        alias='_'
    )

