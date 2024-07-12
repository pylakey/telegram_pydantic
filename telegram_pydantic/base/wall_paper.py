from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# WallPaper - Layer 181
WallPaper = typing.Annotated[
    typing.Union[
        typing.Annotated[types.WallPaper, pydantic.Tag('WallPaper')],
        typing.Annotated[types.WallPaperNoFile, pydantic.Tag('WallPaperNoFile')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
