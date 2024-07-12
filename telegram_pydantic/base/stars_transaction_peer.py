from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# StarsTransactionPeer - Layer 181
StarsTransactionPeer = typing.Annotated[
    typing.Union[
        typing.Annotated[types.StarsTransactionPeer, pydantic.Tag('StarsTransactionPeer')],
        typing.Annotated[types.StarsTransactionPeerAppStore, pydantic.Tag('StarsTransactionPeerAppStore')],
        typing.Annotated[types.StarsTransactionPeerFragment, pydantic.Tag('StarsTransactionPeerFragment')],
        typing.Annotated[types.StarsTransactionPeerPlayMarket, pydantic.Tag('StarsTransactionPeerPlayMarket')],
        typing.Annotated[types.StarsTransactionPeerPremiumBot, pydantic.Tag('StarsTransactionPeerPremiumBot')],
        typing.Annotated[types.StarsTransactionPeerUnsupported, pydantic.Tag('StarsTransactionPeerUnsupported')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
