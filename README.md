# AI Voice Batch Engine

A production-oriented offline Text-to-Speech architecture built with
Python, Piper, OpenVoice and FFmpeg.

This repository contains a **sanitized portfolio edition** of a larger
desktop application developed for high-volume personalized audio generation.

> **Portfolio note:** Proprietary business logic, customer data, production
> configuration, voice models and internal integrations are intentionally excluded.

## Overview

The original system was designed to generate large batches of personalized
audio while efficiently using available CPU and memory resources.

The production architecture combines offline neural TTS, audio processing,
multi-level caching, concurrent execution, optional voice conversion,
performance monitoring and LAN-based distributed processing.

## Architecture

```text
Input Data
    |
    v
Text Normalization
    |
    v
Piper TTS
    |
    v
PCM / Audio Cache
    |
    v
Optional Voice Conversion (OpenVoice)
    |
    v
Audio Processing
    |
    v
FFmpeg
    |
    +-- WAV
    +-- GSM
    +-- MP3
```

## Technologies

- Python
- Piper TTS
- OpenVoice
- FFmpeg
- NumPy / Pandas
- Multiprocessing and threading
- SQLite
- Local network processing

## Engineering Highlights

**Offline TTS.** Neural speech generation is performed locally with Piper,
avoiding dependence on cloud TTS APIs.

**Voice conversion.** The production system can use OpenVoice in an isolated
environment so its dependencies remain separated from the main application.

**Concurrent processing.** Large audio campaigns can be divided among worker
processes according to available computing resources.

**Caching.** The production architecture reuses previously generated artifacts
to reduce repeated synthesis and voice-conversion work.

**Performance monitoring.** The full application records processing time,
voice-conversion time, queue time, cache behavior, worker utilization and
campaign throughput.

**Distributed processing.** The production version can use authorized
computers on the same LAN as additional processing nodes. Networking,
authentication and job-distribution code is not included here.

## Public Repository Structure

```text
ai-voice-batch-engine/
├── src/voice_engine/
│   ├── __init__.py
│   ├── engine.py
│   ├── normalizer.py
│   └── audio.py
├── examples/
│   └── basic_usage.py
├── docs/
│   └── architecture.md
├── screenshots/
├── requirements.txt
├── .gitignore
└── README.md
```

## Example

```python
from voice_engine import VoiceEngine

engine = VoiceEngine("models/es_MX-demo.onnx")
engine.load()

engine.synthesize(
    "Hola, esta es una prueba del motor de voz.",
    "output/demo.wav",
)
```

## Production vs. Portfolio Edition

This repository demonstrates selected architecture and engineering concepts.
The complete application additionally contains advanced cache orchestration,
batch processing, resource management, desktop UI, voice-conversion services,
persistence, detailed performance metrics and distributed LAN processing.

Those production components are intentionally not published in full.

## Project Focus

The engineering goals of the project include:

- local AI inference
- performance and concurrency
- reusable audio fragments
- efficient resource utilization
- fault handling
- scalable batch processing

## Status

Active development. A standalone TTS engine is also being developed to
separate the voice-generation layer from the original desktop application.
