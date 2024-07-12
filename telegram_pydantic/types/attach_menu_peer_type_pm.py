from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class AttachMenuPeerTypePM(BaseModel):
    """
    types.AttachMenuPeerTypePM
    ID: 0xf146d31f
    Layer: 181
    """
    QUALNAME: typing.Literal['types.AttachMenuPeerTypePM', 'AttachMenuPeerTypePM'] = pydantic.Field(
        'types.AttachMenuPeerTypePM',
        alias='_'
    )

