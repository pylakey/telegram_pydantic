from telegram_pydantic.core import BaseModel


def base_type_discriminator(v: dict) -> str | None:
    if isinstance(v, dict):
        return v.get('_', "").split('.')[-1] or v.get('QUALNAME', "").split('.')[-1] or None
    elif isinstance(v, BaseModel):
        return getattr(v, 'QUALNAME', "").split('.')[-1] or getattr(v, '_', "").split('.')[-1] or None

    return None
