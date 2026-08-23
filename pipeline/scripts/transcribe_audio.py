import json, sys, os
from faster_whisper import WhisperModel

print("Loading Whisper model...")
model = WhisperModel("base", device="cpu", compute_type="int8")

def transcribe(audio_path, output_json_path, language=None):
    print(f"Transcribing {audio_path} (lang={language})...")
    segments, info = model.transcribe(audio_path, language=language, beam_size=5)
    results = []
    for s in segments:
        m, sec = divmod(int(s.start), 60)
        time_str = f"{m:02d}:{sec:02d}"
        results.append({
            "start": round(s.start, 2),
            "end": round(s.end, 2),
            "timestamp": time_str,
            "text": s.text.strip()
        })
        print(f"[{time_str}] {s.text.strip()}")
    with open(output_json_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    print(f"Saved {len(results)} segments to {output_json_path}")

en_audio = "evs/downstream/unit_1/assets/unit1_english_audio.m4a"
hi_audio = "evs/downstream/unit_1/assets/unit1_hindi_audio.m4a"

if os.path.exists(en_audio):
    transcribe(en_audio, ".scratch/transcript_english.json", language="en")

if os.path.exists(hi_audio):
    transcribe(hi_audio, ".scratch/transcript_hindi.json", language="hi")

print("Transcription complete!")
