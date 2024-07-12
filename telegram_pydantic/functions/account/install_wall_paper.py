from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InstallWallPaper(BaseModel):
    """
    functions.account.InstallWallPaper
    ID: 0xfeed5769
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.account.InstallWallPaper', 'InstallWallPaper'] = pydantic.Field(
        'functions.account.InstallWallPaper',
        alias='_'
    )

    wallpaper: "base.InputWallPaper"
    settings: "base.WallPaperSettings"
