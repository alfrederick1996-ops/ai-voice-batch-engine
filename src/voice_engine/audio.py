from pathlib import Path
import subprocess


def convert_audio(input_file: str, output_file: str, sample_rate: int = 8000) -> Path:
    """Demonstrate the FFmpeg conversion stage used by the audio pipeline."""
    source = Path(input_file)
    destination = Path(output_file)

    if not source.exists():
        raise FileNotFoundError(source)

    destination.parent.mkdir(parents=True, exist_ok=True)

    command = [
        "ffmpeg", "-y",
        "-i", str(source),
        "-ar", str(sample_rate),
        str(destination),
    ]

    subprocess.run(
        command,
        check=True,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    return destination
