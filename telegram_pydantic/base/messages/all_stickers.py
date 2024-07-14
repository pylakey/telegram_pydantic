from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.AllStickers - Layer 181
AllStickers = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.messages.AllStickers,
            pydantic.Tag('messages.AllStickers'),
            pydantic.Tag('AllStickers')
        ],
        typing.Annotated[
            types.messages.AllStickersNotModified,
            pydantic.Tag('messages.AllStickersNotModified'),
            pydantic.Tag('AllStickersNotModified')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
