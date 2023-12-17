import whisper

model = whisper.load_model("base")
# 这里是 .mp3 或者 .mp4 都可以
result = model.transcribe("./demo/tiktok.m4a", fp16=False, language='English')

# print(result["text"])

# 将结果保存到文本文件
with open('transcription.txt', 'w') as f:
    f.write(result["text"])
