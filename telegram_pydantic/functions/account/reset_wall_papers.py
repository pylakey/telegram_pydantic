from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ResetWallPapers(BaseModel):
    """
    functions.account.ResetWallPapers
    ID: 0xbb3b9804
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.ResetWallPapers', 'ResetWallPapers'] = pydantic.Field(
        'functions.account.ResetWallPapers',
        alias='_'
    )

