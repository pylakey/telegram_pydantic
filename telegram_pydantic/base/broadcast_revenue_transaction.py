from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# BroadcastRevenueTransaction - Layer 181
BroadcastRevenueTransaction = typing.Annotated[
    typing.Union[
        typing.Annotated[types.BroadcastRevenueTransactionProceeds, pydantic.Tag('BroadcastRevenueTransactionProceeds')],
        typing.Annotated[types.BroadcastRevenueTransactionRefund, pydantic.Tag('BroadcastRevenueTransactionRefund')],
        typing.Annotated[types.BroadcastRevenueTransactionWithdrawal, pydantic.Tag('BroadcastRevenueTransactionWithdrawal')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
