from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# WebPage - Layer 181
WebPage = typing.Annotated[
    typing.Union[
        typing.Annotated[types.WebPage, pydantic.Tag('WebPage')],
        typing.Annotated[types.WebPageEmpty, pydantic.Tag('WebPageEmpty')],
        typing.Annotated[types.WebPageNotModified, pydantic.Tag('WebPageNotModified')],
        typing.Annotated[types.WebPagePending, pydantic.Tag('WebPagePending')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
