from faster_whisper import WhisperModel
import sys

print("Loading Whisper model base...", flush=True)
model = WhisperModel("base", device="cpu", compute_type="int8")

hi_audio = "evs/downstream/unit_1/assets/unit1_hindi_audio.m4a"
print("Transcribing first few chunks with initial_prompt...", flush=True)

segments, info = model.transcribe(
    hi_audio, 
    language="hi", 
    initial_prompt="नमस्ते, यह कक्षा 3, 4, 5 के पर्यावरण अध्ययन और सजीव जगत, पशु व्यवहार, स्लॉथ, हाथी, बाघ की हिंदी परिचर्चा है।",
    beam_size=1
)

for idx, s in enumerate(segments):
    print(f"Segment {idx} [{s.start:.2f}s - {s.end:.2f}s]: {s.text}", flush=True)
    if idx >= 5:
        break
print("Done test.", flush=True)
