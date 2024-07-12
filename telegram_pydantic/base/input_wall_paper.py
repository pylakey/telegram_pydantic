from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputWallPaper - Layer 181
InputWallPaper = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputWallPaper, pydantic.Tag('InputWallPaper')],
        typing.Annotated[types.InputWallPaperNoFile, pydantic.Tag('InputWallPaperNoFile')],
        typing.Annotated[types.InputWallPaperSlug, pydantic.Tag('InputWallPaperSlug')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
