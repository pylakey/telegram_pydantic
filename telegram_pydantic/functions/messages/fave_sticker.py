from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class FaveSticker(BaseModel):
    """
    functions.messages.FaveSticker
    ID: 0xb9ffc55b
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.FaveSticker', 'FaveSticker'] = pydantic.Field(
        'functions.messages.FaveSticker',
        alias='_'
    )

    id: "base.InputDocument"
    unfave: bool
