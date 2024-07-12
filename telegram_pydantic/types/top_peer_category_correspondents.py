from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class TopPeerCategoryCorrespondents(BaseModel):
    """
    types.TopPeerCategoryCorrespondents
    ID: 0x637b7ed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.TopPeerCategoryCorrespondents', 'TopPeerCategoryCorrespondents'] = pydantic.Field(
        'types.TopPeerCategoryCorrespondents',
        alias='_'
    )

