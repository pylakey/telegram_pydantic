from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# DialogFilter - Layer 181
DialogFilter = typing.Annotated[
    typing.Union[
        typing.Annotated[types.DialogFilter, pydantic.Tag('DialogFilter')],
        typing.Annotated[types.DialogFilterChatlist, pydantic.Tag('DialogFilterChatlist')],
        typing.Annotated[types.DialogFilterDefault, pydantic.Tag('DialogFilterDefault')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
