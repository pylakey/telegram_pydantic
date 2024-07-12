from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SetChatWallPaper(BaseModel):
    """
    functions.messages.SetChatWallPaper
    ID: 0x8ffacae1
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.messages.SetChatWallPaper', 'SetChatWallPaper'] = pydantic.Field(
        'functions.messages.SetChatWallPaper',
        alias='_'
    )

    peer: "base.InputPeer"
    for_both: typing.Optional[bool] = None
    revert: typing.Optional[bool] = None
    wallpaper: typing.Optional["base.InputWallPaper"] = None
    settings: typing.Optional["base.WallPaperSettings"] = None
    id: typing.Optional[int] = None
