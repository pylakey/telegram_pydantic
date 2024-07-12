from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# Dialog - Layer 181
Dialog = typing.Annotated[
    typing.Union[
        typing.Annotated[types.Dialog, pydantic.Tag('Dialog')],
        typing.Annotated[types.DialogFolder, pydantic.Tag('DialogFolder')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
