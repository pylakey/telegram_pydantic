from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputStickeredMediaPhoto(BaseModel):
    """
    types.InputStickeredMediaPhoto
    ID: 0x4a992157
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputStickeredMediaPhoto', 'InputStickeredMediaPhoto'] = pydantic.Field(
        'types.InputStickeredMediaPhoto',
        alias='_'
    )

    id: "base.InputPhoto"
