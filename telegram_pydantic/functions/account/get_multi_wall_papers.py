from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetMultiWallPapers(BaseModel):
    """
    functions.account.GetMultiWallPapers
    ID: 0x65ad71dc
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.GetMultiWallPapers', 'GetMultiWallPapers'] = pydantic.Field(
        'functions.account.GetMultiWallPapers',
        alias='_'
    )

    wallpapers: list["base.InputWallPaper"]
