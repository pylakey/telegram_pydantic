from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class SendMessageUploadDocumentAction(BaseModel):
    """
    types.SendMessageUploadDocumentAction
    ID: 0xaa0cd9e4
    Layer: 181
    """
    QUALNAME: typing.Literal['types.SendMessageUploadDocumentAction', 'SendMessageUploadDocumentAction'] = pydantic.Field(
        'types.SendMessageUploadDocumentAction',
        alias='_'
    )

    progress: int
