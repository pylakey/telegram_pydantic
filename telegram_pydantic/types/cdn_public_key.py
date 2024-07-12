from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class CdnPublicKey(BaseModel):
    """
    types.CdnPublicKey
    ID: 0xc982eaba
    Layer: 181
    """
    QUALNAME: typing.Literal['types.CdnPublicKey', 'CdnPublicKey'] = pydantic.Field(
        'types.CdnPublicKey',
        alias='_'
    )

    dc_id: int
    public_key: str
