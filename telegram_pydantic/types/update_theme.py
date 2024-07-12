from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class UpdateTheme(BaseModel):
    """
    types.UpdateTheme
    ID: 0x8216fba3
    Layer: 181
    """
    QUALNAME: typing.Literal['types.UpdateTheme', 'UpdateTheme'] = pydantic.Field(
        'types.UpdateTheme',
        alias='_'
    )

    theme: "base.Theme"
