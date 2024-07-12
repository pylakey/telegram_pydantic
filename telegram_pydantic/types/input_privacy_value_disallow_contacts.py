from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class InputPrivacyValueDisallowContacts(BaseModel):
    """
    types.InputPrivacyValueDisallowContacts
    ID: 0xba52007
    Layer: 181
    """
    QUALNAME: typing.Literal['types.InputPrivacyValueDisallowContacts', 'InputPrivacyValueDisallowContacts'] = pydantic.Field(
        'types.InputPrivacyValueDisallowContacts',
        alias='_'
    )

