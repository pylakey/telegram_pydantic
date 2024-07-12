from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputDialogPeer(BaseModel):
    """
    types.InputDialogPeer
    ID: 0xfcaafeb7
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputDialogPeer', 'InputDialogPeer'] = pydantic.Field(
        'types.InputDialogPeer',
        alias='_'
    )

    peer: "base.InputPeer"
