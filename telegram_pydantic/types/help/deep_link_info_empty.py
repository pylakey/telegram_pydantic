from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class DeepLinkInfoEmpty(BaseModel):
    """
    types.help.DeepLinkInfoEmpty
    ID: 0x66afa166
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.DeepLinkInfoEmpty', 'DeepLinkInfoEmpty'] = pydantic.Field(
        'types.help.DeepLinkInfoEmpty',
        alias='_'
    )

