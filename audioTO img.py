from PIL import Image
from pydub import AudioSegment

# Load an audio file
audio = AudioSegment.from_file("input_audio.wav", format="wav")

# Convert the audio to a bytes string
audio_data = audio.raw_data

# Create an image from the audio data
image = Image.frombytes("RGB", (1, len(audio_data) // 3), audio_data)

# Save the image to a file
image.save("output_image.png", "PNG")
