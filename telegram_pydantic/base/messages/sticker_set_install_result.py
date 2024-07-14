from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# messages.StickerSetInstallResult - Layer 181
StickerSetInstallResult = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.messages.StickerSetInstallResultArchive,
            pydantic.Tag('messages.StickerSetInstallResultArchive'),
            pydantic.Tag('StickerSetInstallResultArchive')
        ],
        typing.Annotated[
            types.messages.StickerSetInstallResultSuccess,
            pydantic.Tag('messages.StickerSetInstallResultSuccess'),
            pydantic.Tag('StickerSetInstallResultSuccess')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
