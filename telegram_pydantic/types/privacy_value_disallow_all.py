from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueDisallowAll(BaseModel):
    """
    types.PrivacyValueDisallowAll
    ID: 0x8b73e763
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueDisallowAll', 'PrivacyValueDisallowAll'] = pydantic.Field(
        'types.PrivacyValueDisallowAll',
        alias='_'
    )

