from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputFile - Layer 181
InputFile = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputFile, pydantic.Tag('InputFile')],
        typing.Annotated[types.InputFileBig, pydantic.Tag('InputFileBig')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
