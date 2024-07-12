from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class Themes(BaseModel):
    """
    types.account.Themes
    ID: 0x9a3d8c6d
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.Themes', 'Themes'] = pydantic.Field(
        'types.account.Themes',
        alias='_'
    )

    hash: int
    themes: list["base.Theme"]
