# System Architecture

## High-Level Pipeline

```text
Input (CSV / Text / UI)
        |
        v
Text Processing & Normalization
        |
        v
Piper TTS - Local Inference
        |
        v
Audio Cache
        |
        v
Optional OpenVoice Conversion
        |
        v
Audio Processing
        |
        v
FFmpeg
   /     |     \
 WAV    GSM    MP3
```

## Concurrency

The production application distributes synthesis work across multiple worker
processes. This public repository documents the concept without publishing the
complete production orchestration.

```text
              Job Queue
                 |
       +---------+---------+
       |         |         |
       v         v         v
    Worker 1  Worker 2  Worker N
       |         |         |
       +---------+---------+
                 |
                 v
          Generated Audio
```

## Voice Conversion

OpenVoice is isolated from the main TTS environment to reduce dependency
conflicts.

```text
Main Application
      |
      v
   Piper TTS
      |
      v
Temporary Audio
      |
      v
OpenVoice Service
      |
      v
Converted Voice
```

## Caching

```text
Request
   |
   v
Cache Lookup
   |
   +-- HIT --> Reuse Artifact
   |
   +-- MISS --> Generate --> Store --> Return
```

The complete caching implementation is not part of the portfolio edition.

## Distributed Processing

The production application includes LAN-based workload distribution between
authorized computers. Only the architectural concept is described publicly;
networking, authentication, discovery and production job-distribution
implementation remain private.
