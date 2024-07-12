from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SaveWallPaper(BaseModel):
    """
    functions.account.SaveWallPaper
    ID: 0x6c5a5b37
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.SaveWallPaper', 'SaveWallPaper'] = pydantic.Field(
        'functions.account.SaveWallPaper',
        alias='_'
    )

    wallpaper: "base.InputWallPaper"
    unsave: bool
    settings: "base.WallPaperSettings"
