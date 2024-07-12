from __future__ import annotations

import typing
from datetime import datetime

import pydantic

from telegram_pydantic.core import BaseModel
from telegram_pydantic.primitives import Bytes
from telegram_pydantic.primitives import Datetime

if typing.TYPE_CHECKING:
    from telegram_pydantic import base


class WebPageAttributeTheme(BaseModel):
    """
    types.WebPageAttributeTheme
    ID: 0x54b56617
    Layer: 181
    """
    QUALNAME: typing.Literal['types.WebPageAttributeTheme', 'WebPageAttributeTheme'] = pydantic.Field(
        'types.WebPageAttributeTheme',
        alias='_'
    )

    documents: typing.Optional[list["base.Document"]] = None
    settings: typing.Optional["base.ThemeSettings"] = None
