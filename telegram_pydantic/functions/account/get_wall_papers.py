from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetWallPapers(BaseModel):
    """
    functions.account.GetWallPapers
    ID: 0x7967d36
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetWallPapers', 'GetWallPapers'] = pydantic.Field(
        'functions.account.GetWallPapers',
        alias='_'
    )

    hash: int
