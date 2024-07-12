from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class GetIsPremiumRequiredToContact(BaseModel):
    """
    functions.users.GetIsPremiumRequiredToContact
    ID: 0xa622aa10
    Layer: 181
    """
    QUALNAME: typing.Literal['functions.users.GetIsPremiumRequiredToContact', 'GetIsPremiumRequiredToContact'] = pydantic.Field(
        'functions.users.GetIsPremiumRequiredToContact',
        alias='_'
    )

    id: list["base.InputUser"]
