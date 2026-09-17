from pathlib import Path
from typing import Optional

from piper import PiperVoice

from .normalizer import normalize_text


class VoiceEngine:
    """Simplified public interface for offline neural TTS.

    This portfolio implementation represents selected concepts from
    a larger production-oriented audio generation application.
    Advanced caching, distributed processing, voice conversion and
    internal integrations are intentionally excluded.
    """

    def __init__(self, model_path: str):
        self.model_path = Path(model_path)
        self._voice: Optional[PiperVoice] = None

    def load(self) -> None:
        """Load a local Piper voice model."""
        if not self.model_path.exists():
            raise FileNotFoundError(f"Voice model not found: {self.model_path}")

        self._voice = PiperVoice.load(str(self.model_path))

    @property
    def is_loaded(self) -> bool:
        return self._voice is not None

    def synthesize(self, text: str, output_path: str) -> Path:
        """Generate a WAV file from text."""
        if not self.is_loaded:
            raise RuntimeError("Voice model is not loaded. Call load() first.")

        normalized_text = normalize_text(text)
        if not normalized_text:
            raise ValueError("Text cannot be empty.")

        destination = Path(output_path)
        destination.parent.mkdir(parents=True, exist_ok=True)

        with destination.open("wb") as wav_file:
            self._voice.synthesize_wav(normalized_text, wav_file)

        return destination
