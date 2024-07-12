from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class MissingInvitee(BaseModel):
    """
    types.MissingInvitee
    ID: 0x628c9224
    Layer: 181
    """
    QUALNAME: typing.Literal['types.MissingInvitee', 'MissingInvitee'] = pydantic.Field(
        'types.MissingInvitee',
        alias='_'
    )

    user_id: int
    premium_would_allow_invite: typing.Optional[bool] = None
    premium_required_for_pm: typing.Optional[bool] = None
