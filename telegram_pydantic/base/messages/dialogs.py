from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.Dialogs - Layer 181
Dialogs = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.messages.Dialogs,
            pydantic.Tag('messages.Dialogs'),
            pydantic.Tag('Dialogs')
        ],
        typing.Annotated[
            types.messages.DialogsNotModified,
            pydantic.Tag('messages.DialogsNotModified'),
            pydantic.Tag('DialogsNotModified')
        ],
        typing.Annotated[
            types.messages.DialogsSlice,
            pydantic.Tag('messages.DialogsSlice'),
            pydantic.Tag('DialogsSlice')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
