from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputWallPaperNoFile(BaseModel):
    """
    types.InputWallPaperNoFile
    ID: 0x967a462e
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputWallPaperNoFile', 'InputWallPaperNoFile'] = pydantic.Field(
        'types.InputWallPaperNoFile',
        alias='_'
    )

    id: int
