from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TextWithEntities(BaseModel):
    """
    types.TextWithEntities
    ID: 0x751f3146
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TextWithEntities', 'TextWithEntities'] = pydantic.Field(
        'types.TextWithEntities',
        alias='_'
    )

    text: str
    entities: list["base.MessageEntity"]
