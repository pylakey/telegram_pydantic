from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# contacts.TopPeers - Layer 181
TopPeers = typing.Annotated[
    typing.Union[
        typing.Annotated[
            types.contacts.TopPeers,
            pydantic.Tag('contacts.TopPeers'),
            pydantic.Tag('TopPeers')
        ],
        typing.Annotated[
            types.contacts.TopPeersDisabled,
            pydantic.Tag('contacts.TopPeersDisabled'),
            pydantic.Tag('TopPeersDisabled')
        ],
        typing.Annotated[
            types.contacts.TopPeersNotModified,
            pydantic.Tag('contacts.TopPeersNotModified'),
            pydantic.Tag('TopPeersNotModified')
        ]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
