# Internally, the transcribe() method reads the entire file and processes the audio with a sliding 30-second window, performing autoregressive sequence-to-sequence predictions on each window.
# 在内部， transcribe() 方法读取整个文件并使用滑动的 30 秒窗口处理音频，对每个窗口执行自回归序列到序列预测。

# Below is an example usage of whisper.detect_language() and whisper.decode() which provide lower-level access to the model.
# 下面是 whisper.detect_language() 和 whisper.decode() 的示例用法，它们提供对模型的较低级别访问。

import whisper

model = whisper.load_model("large-v3")

# 这里是 .mp3 或者 .mp4 都可以
# load audio and pad/trim it to fit 30 seconds
audio = whisper.load_audio("./demo/second.mp4")
audio = whisper.pad_or_trim(audio)

# make log-Mel spectrogram and move to the same device as the model
mel = whisper.log_mel_spectrogram(audio).to(model.device)

# detect the spoken language
_, probs = model.detect_language(mel)
print(f"Detected language: {max(probs, key=probs.get)}")

# decode the audio
options = whisper.DecodingOptions()
result = whisper.decode(model, mel, options)

print(result.text)

# 将结果保存到文本文件
with open('second.txt', 'w') as f:
    f.write(result.text)
