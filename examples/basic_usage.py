from voice_engine import VoiceEngine


def main():
    engine = VoiceEngine(model_path="models/es_MX-demo.onnx")
    engine.load()

    output = engine.synthesize(
        text="Hola, esta es una demostración del motor de voz.",
        output_path="output/demo.wav",
    )
    print(f"Audio generated: {output}")


if __name__ == "__main__":
    main()
