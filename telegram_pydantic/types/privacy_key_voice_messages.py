from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PrivacyKeyVoiceMessages(BaseModel):
    """
    types.PrivacyKeyVoiceMessages
    ID: 0x697f414
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PrivacyKeyVoiceMessages', 'PrivacyKeyVoiceMessages'] = pydantic.Field(
        'types.PrivacyKeyVoiceMessages',
        alias='_'
    )

