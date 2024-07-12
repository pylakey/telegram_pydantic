from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPaperNoFile(BaseModel):
    """
    types.WallPaperNoFile
    ID: 0xe0804116
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WallPaperNoFile', 'WallPaperNoFile'] = pydantic.Field(
        'types.WallPaperNoFile',
        alias='_'
    )

    id: int
    default: typing.Optional[bool] = None
    dark: typing.Optional[bool] = None
    settings: typing.Optional["base.WallPaperSettings"] = None
