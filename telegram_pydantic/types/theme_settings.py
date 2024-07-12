from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ThemeSettings(BaseModel):
    """
    types.ThemeSettings
    ID: 0xfa58b6d4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.ThemeSettings', 'ThemeSettings'] = pydantic.Field(
        'types.ThemeSettings',
        alias='_'
    )

    base_theme: "base.BaseTheme"
    accent_color: int
    message_colors_animated: typing.Optional[bool] = None
    outbox_accent_color: typing.Optional[int] = None
    message_colors: typing.Optional[list[int]] = None
    wallpaper: typing.Optional["base.WallPaper"] = None
