# from PIL import Image
# from pydub import AudioSegment

# # Load an image
# image = Image.open("audio conversion/00000064_20231017_155056126.jpeg")

# # Convert the image to a string
# image_data = image.tobytes()

# # Create an AudioSegment from the image data
# audio = AudioSegment.from_bytes(image_data)

# # Export the audio to a file
# audio.export("output_audio.wav", format="wav")


# from PIL import Image
# import numpy as np
# import scipy.io.wavfile as wav

# # Load an image
# image = Image.open("audio conversion/00000064_20231017_155056126.jpeg")

# # Convert the image to a numpy array
# image_data = np.array(image)

# # Normalize the pixel values
# normalized_data = image_data / 255.0

# # Convert the image data to a 1D array and rescale it to audio range
# audio_data = normalized_data.ravel()

# # Set the sample rate (you can adjust this value)
# sample_rate = 44100

# # Save the audio data to a WAV file
# wav.write("output_audio.mp4", sample_rate, audio_data)


# import numpy as np
# import librosa.display
# import matplotlib.pyplot as plt

# # Load an image
# image = Image.open("audio conversion/00000064_20231017_155056126.jpeg")

# # Convert the image to a numpy array
# image_data = np.array(image)

# # Normalize the pixel values
# normalized_data = image_data / 255.0

# # Convert the image data back into audio using librosa
# y, sr = librosa.core.load("output_audio.wav", sr=44100)  # Adjust the sample rate as needed

# # Plot the spectrogram to visualize the result
# librosa.display.specshow(librosa.amplitude_to_db(np.abs(librosa.stft(y)), ref=np.max), y_axis='log', x_axis='time')
# plt.colorbar(format='%+2.0f dB')
# plt.show()


# from PIL import Image
# import numpy as np
# import librosa.display
# import matplotlib.pyplot as plt
# from moviepy.editor import VideoFileClip, AudioFileClip, VideoClip
# from moviepy.editor import concatenate_videoclips

# # Rest of your code...


# # Rest of your code here...

# # from moviepy.editor import VideoFileClip, AudioFileClip
# # from moviepy.editor import concatenate_videoclips

# # Load your image
# image = Image.open("audio conversion/00000064_20231017_155056126.jpeg")

# # Create a function to generate the video frames
# def make_frame(t):
#     return np.array(image)

# # Create a VideoClip with the frame generation function
# clip = VideoClip(make_frame, duration=5)  # Adjust the duration as needed

# # Export the video to an MP4 file
# video_path = "output_video.mp4"
# clip.write_videofile(video_path, codec="libx264")

# # Load the video clip and extract the audio
# video_clip = VideoFileClip(video_path)
# audio_clip = video_clip.audio

# # Export the audio as an MP4 file
# audio_clip.write_audiofile("output_audio.mp4", codec="aac")





from PIL import Image
import numpy as np
from moviepy.editor import VideoClip
from moviepy.editor import concatenate_videoclips

# Load your image
image = Image.open("audio conversion/00000064_20231017_155056126.jpeg")

# Create a function to generate the video frames
def make_frame(t):
    return np.array(image)

# Set the frames per second (adjust as needed)
fps = 1
  # You can change this value

# Create a VideoClip with the frame generation function and fps setting
clip = VideoClip(make_frame, duration=5, fps=fps)  # Adjust the duration as needed

# Export the video to an MP4 file
video_path = "output_video.mp4"
clip.write_videofile(video_path, codec="libx264")
