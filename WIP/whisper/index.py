import whisper

model = whisper.load_model("large-v3")
# 这里是 .mp3 或者 .mp4 都可以
result = model.transcribe("./demo/0401680564.mp3", fp16=False)

print(result["text"])

# 将结果保存到文本文件
with open('0401680564.txt', 'w') as f:
    f.write(result["text"])
