from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WallPapers(BaseModel):
    """
    types.account.WallPapers
    ID: 0xcdc3858c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.WallPapers', 'WallPapers'] = pydantic.Field(
        'types.account.WallPapers',
        alias='_'
    )

    hash: int
    wallpapers: list["base.WallPaper"]
