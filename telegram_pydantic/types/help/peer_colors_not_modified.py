from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PeerColorsNotModified(BaseModel):
    """
    types.help.PeerColorsNotModified
    ID: 0x2ba1f5ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PeerColorsNotModified', 'PeerColorsNotModified'] = pydantic.Field(
        'types.help.PeerColorsNotModified',
        alias='_'
    )

