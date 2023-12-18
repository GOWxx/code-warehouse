import whisper

model = whisper.load_model("base")
# 这里是 .mp3 或者 .mp4 都可以
result = model.transcribe("./demo/Test1.Section1.mp3", fp16=False)

print(result["text"])

# 将结果保存到文本文件
with open('Test1.Section1.txt', 'w') as f:
    f.write(result["text"])
