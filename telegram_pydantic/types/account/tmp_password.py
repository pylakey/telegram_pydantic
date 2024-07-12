from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TmpPassword(BaseModel):
    """
    types.account.TmpPassword
    ID: 0xdb64fd34
    Layer: 181
    """
    QUALNAME: typing.Literal['types.account.TmpPassword', 'TmpPassword'] = pydantic.Field(
        'types.account.TmpPassword',
        alias='_'
    )

    tmp_password: Bytes
    valid_until: Datetime
