import whisper

model = whisper.load_model("base")
# 这里是 .mp3 或者 .mp4 都可以
result = model.transcribe("./demo/audio_test.mp4", fp16=False, language='English')
print(result["text"])
