from __future__ import annotations

import typing

import pydantic

from telegram_pydantic import types
from telegram_pydantic.utils import base_type_discriminator

# PageBlock - Layer 181
PageBlock = typing.Annotated[
    typing.Union[
        typing.Annotated[types.PageBlockAnchor, pydantic.Tag('PageBlockAnchor')],
        typing.Annotated[types.PageBlockAudio, pydantic.Tag('PageBlockAudio')],
        typing.Annotated[types.PageBlockAuthorDate, pydantic.Tag('PageBlockAuthorDate')],
        typing.Annotated[types.PageBlockBlockquote, pydantic.Tag('PageBlockBlockquote')],
        typing.Annotated[types.PageBlockChannel, pydantic.Tag('PageBlockChannel')],
        typing.Annotated[types.PageBlockCollage, pydantic.Tag('PageBlockCollage')],
        typing.Annotated[types.PageBlockCover, pydantic.Tag('PageBlockCover')],
        typing.Annotated[types.PageBlockDetails, pydantic.Tag('PageBlockDetails')],
        typing.Annotated[types.PageBlockDivider, pydantic.Tag('PageBlockDivider')],
        typing.Annotated[types.PageBlockEmbed, pydantic.Tag('PageBlockEmbed')],
        typing.Annotated[types.PageBlockEmbedPost, pydantic.Tag('PageBlockEmbedPost')],
        typing.Annotated[types.PageBlockFooter, pydantic.Tag('PageBlockFooter')],
        typing.Annotated[types.PageBlockHeader, pydantic.Tag('PageBlockHeader')],
        typing.Annotated[types.PageBlockKicker, pydantic.Tag('PageBlockKicker')],
        typing.Annotated[types.PageBlockList, pydantic.Tag('PageBlockList')],
        typing.Annotated[types.PageBlockMap, pydantic.Tag('PageBlockMap')],
        typing.Annotated[types.PageBlockOrderedList, pydantic.Tag('PageBlockOrderedList')],
        typing.Annotated[types.PageBlockParagraph, pydantic.Tag('PageBlockParagraph')],
        typing.Annotated[types.PageBlockPhoto, pydantic.Tag('PageBlockPhoto')],
        typing.Annotated[types.PageBlockPreformatted, pydantic.Tag('PageBlockPreformatted')],
        typing.Annotated[types.PageBlockPullquote, pydantic.Tag('PageBlockPullquote')],
        typing.Annotated[types.PageBlockRelatedArticles, pydantic.Tag('PageBlockRelatedArticles')],
        typing.Annotated[types.PageBlockSlideshow, pydantic.Tag('PageBlockSlideshow')],
        typing.Annotated[types.PageBlockSubheader, pydantic.Tag('PageBlockSubheader')],
        typing.Annotated[types.PageBlockSubtitle, pydantic.Tag('PageBlockSubtitle')],
        typing.Annotated[types.PageBlockTable, pydantic.Tag('PageBlockTable')],
        typing.Annotated[types.PageBlockTitle, pydantic.Tag('PageBlockTitle')],
        typing.Annotated[types.PageBlockUnsupported, pydantic.Tag('PageBlockUnsupported')],
        typing.Annotated[types.PageBlockVideo, pydantic.Tag('PageBlockVideo')]
    ],
    pydantic.Discriminator(base_type_discriminator)
]
