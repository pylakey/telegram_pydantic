from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PostAddress(BaseModel):
    """
    types.PostAddress
    ID: 0x1e8caaeb
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PostAddress', 'PostAddress'] = pydantic.Field(
        'types.PostAddress',
        alias='_'
    )

    street_line1: str
    street_line2: str
    city: str
    state: str
    country_iso2: str
    post_code: str
