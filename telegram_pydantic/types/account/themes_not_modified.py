from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ThemesNotModified(BaseModel):
    """
    types.account.ThemesNotModified
    ID: 0xf41eb622
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.ThemesNotModified', 'ThemesNotModified'] = pydantic.Field(
        'types.account.ThemesNotModified',
        alias='_'
    )

