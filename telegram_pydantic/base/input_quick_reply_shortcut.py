from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# InputQuickReplyShortcut - Layer 181
InputQuickReplyShortcut = typing.Annotated[
    typing.Union[
        typing.Annotated[types.InputQuickReplyShortcut, pydantic.Tag('InputQuickReplyShortcut')],
        typing.Annotated[types.InputQuickReplyShortcutId, pydantic.Tag('InputQuickReplyShortcutId')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
