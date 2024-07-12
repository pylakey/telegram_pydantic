from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class ExportedGroupCallInvite(BaseModel):
    """
    types.phone.ExportedGroupCallInvite
    ID: 0x204bd158
    Layer: 181
    """
    QUALNAME: typing.Literal['types.phone.ExportedGroupCallInvite', 'ExportedGroupCallInvite'] = pydantic.Field(
        'types.phone.ExportedGroupCallInvite',
        alias='_'
    )

    link: str
