from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# help.PeerColors - Layer 181
PeerColors = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.help.PeerColors,
            pydantic.Tag('help.PeerColors'),
            pydantic.Tag('PeerColors')
        ],
        typing.Annotated[
            types.help.PeerColorsNotModified,
            pydantic.Tag('help.PeerColorsNotModified'),
            pydantic.Tag('PeerColorsNotModified')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
