from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnConfig(BaseModel):
    """
    types.CdnConfig
    ID: 0x5725e40a
    Layer: 181
    """
    QUALNAME: typing.Literal['types.CdnConfig', 'CdnConfig'] = pydantic.Field(
        'types.CdnConfig',
        alias='_'
    )

    public_keys: list["base.CdnPublicKey"]
