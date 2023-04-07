from moviepy.editor import AudioFileClip
from pydub.utils import mediainfo

def convert(mp4_path, new_path):
    audio = AudioFileClip(mp4_path)
    bitrate = mediainfo(mp4_path)["bit_rate"]
    audio.write_audiofile(new_path, bitrate=bitrate)
    audio.close()