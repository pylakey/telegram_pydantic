def base_type_discriminator(v: dict) -> str | None:
    if isinstance(v, dict):
        return v.get('_', "").split('.')[-1] or None

    return None
