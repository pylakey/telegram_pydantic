from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueAllowContacts(BaseModel):
    """
    types.InputPrivacyValueAllowContacts
    ID: 0xd09e07b
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueAllowContacts', 'InputPrivacyValueAllowContacts'] = pydantic.Field(
        'types.InputPrivacyValueAllowContacts',
        alias='_'
    )

