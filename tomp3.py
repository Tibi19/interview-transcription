from moviepy.editor import AudioFileClip
from pydub.utils import mediainfo
from pydub import AudioSegment

def convert_m4a(m4a_path, new_path) -> str:
    audio = AudioSegment.from_file(m4a_path, format="m4a")
    audio.export(new_path, format="mp3")

    return new_path

def convert_mp4(mp4_path, new_path) -> str:
    audio = AudioFileClip(mp4_path)
    bitrate = mediainfo(mp4_path)["bit_rate"]
    audio.write_audiofile(new_path, bitrate=bitrate)
    audio.close()

    return new_path
