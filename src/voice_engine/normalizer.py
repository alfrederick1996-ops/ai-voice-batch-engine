import re


def normalize_text(text: str) -> str:
    """Prepare text before sending it to the TTS engine.

    The production version contains additional rules for numbers,
    dates, currencies and application-specific text formats.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    text = text.replace("…", "...")
    text = text.replace("“", '"').replace("”", '"')
    text = text.replace("’", "'")
    return text
