from nexa.gguf import NexaVoiceInference

model_path = "./models/OmniAudio.gguf"
inference = NexaVoiceInference(
    model_path=model_path,
    local_path=True,
    beam_size=5,
    language=None,
    task="transcribe",
    temperature=0.0,
    compute_type="default"
)

# run() method
inference.run()

# run_streamlit() method
inference.run_streamlit()

# _transcribe_audio(audio_path) method
inference.transcribe("path/to/your/audio.wav")