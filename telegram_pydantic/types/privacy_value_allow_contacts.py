from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyValueAllowContacts(BaseModel):
    """
    types.PrivacyValueAllowContacts
    ID: 0xfffe1bac
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyValueAllowContacts', 'PrivacyValueAllowContacts'] = pydantic.Field(
        'types.PrivacyValueAllowContacts',
        alias='_'
    )

