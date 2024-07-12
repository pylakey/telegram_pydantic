from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class PageBlockParagraph(BaseModel):
    """
    types.PageBlockParagraph
    ID: 0x467a0766
    Layer: 181
    """
    QUALNAME: typing.Literal['types.PageBlockParagraph', 'PageBlockParagraph'] = pydantic.Field(
        'types.PageBlockParagraph',
        alias='_'
    )

    text: "base.RichText"
