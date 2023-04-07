from pydub import AudioSegment
from pydub.utils import mediainfo

def get_audio(from_path):
    _, extension = from_path.split('.')
    if extension == "mp3":
        return AudioSegment.from_mp3(from_path)
    if extension == "m4a":
        return AudioSegment.from_file(from_path, format="m4a")

# @divisions - At what times to divide the recording in format xx:xx e.g. divisions = ["1:54", "11:20", "21:03"]
def divide(from_path, to_path_beginning, divisions) -> list[str]:
    audio = get_audio(from_path)
    bitrate = mediainfo(from_path)["bit_rate"]

    new_paths = []
    last_ms_division = 0
    length = len(divisions)
    for i in range(length):
        division = divisions[i]
        minutes_str, seconds_str = division.split(":")
        minutes = int(minutes_str)
        seconds = int(seconds_str)
        divide_at_ms = minutes * 60 * 1000 + seconds * 1000

        audio_division = audio[last_ms_division:divide_at_ms]
        division_name = f'{to_path_beginning}_div{i+1}.mp3'
        audio_division.export(division_name, format="mp3", bitrate=bitrate)

        new_paths.append(division_name)
        last_ms_division = divide_at_ms

    last_audio_division = audio[last_ms_division:]
    last_division_name = f'{to_path_beginning}_div{length+1}.mp3'
    last_audio_division.export(last_division_name, format="mp3", bitrate=bitrate)
    new_paths.append(last_division_name)

    return new_paths

