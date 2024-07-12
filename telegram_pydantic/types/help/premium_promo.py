from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PremiumPromo(BaseModel):
    """
    types.help.PremiumPromo
    ID: 0x5334759c
    Layer: 181
    """
    QUALNAME: typing.Literal['types.help.PremiumPromo', 'PremiumPromo'] = pydantic.Field(
        'types.help.PremiumPromo',
        alias='_'
    )

    status_text: str
    status_entities: list["base.MessageEntity"]
    video_sections: list[str]
    videos: list["base.Document"]
    period_options: list["base.PremiumSubscriptionOption"]
    users: list["base.User"]
