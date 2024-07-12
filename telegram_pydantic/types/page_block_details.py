from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockDetails(BaseModel):
    """
    types.PageBlockDetails
    ID: 0x76768bed
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockDetails', 'PageBlockDetails'] = pydantic.Field(
        'types.PageBlockDetails',
        alias='_'
    )

    blocks: list["base.PageBlock"]
    title: "base.RichText"
    open: typing.Optional[bool] = None
