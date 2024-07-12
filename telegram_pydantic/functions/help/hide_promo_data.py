from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class HidePromoData(BaseModel):
    """
    functions.help.HidePromoData
    ID: 0x1e251c95
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.help.HidePromoData', 'HidePromoData'] = pydantic.Field(
        'functions.help.HidePromoData',
        alias='_'
    )

    peer: "base.InputPeer"
