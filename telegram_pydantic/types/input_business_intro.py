from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputBusinessIntro(BaseModel):
    """
    types.InputBusinessIntro
    ID: 0x9c469cd
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputBusinessIntro', 'InputBusinessIntro'] = pydantic.Field(
        'types.InputBusinessIntro',
        alias='_'
    )

    title: str
    description: str
    sticker: typing.Optional["base.InputDocument"] = None
