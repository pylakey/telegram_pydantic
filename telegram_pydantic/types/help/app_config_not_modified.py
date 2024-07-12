from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AppConfigNotModified(BaseModel):
    """
    types.help.AppConfigNotModified
    ID: 0x7cde641d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.AppConfigNotModified', 'AppConfigNotModified'] = pydantic.Field(
        'types.help.AppConfigNotModified',
        alias='_'
    )

