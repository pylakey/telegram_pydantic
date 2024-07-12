from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowAll(BaseModel):
    """
    types.InputPrivacyValueAllowAll
    ID: 0x184b35ce
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowAll', 'InputPrivacyValueAllowAll'] = pydantic.Field(
        'types.InputPrivacyValueAllowAll',
        alias='_'
    )

