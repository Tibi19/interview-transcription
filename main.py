import tomp3
import split
import transc

# INPUT

audio_paths = []
divisions_timestamps = []
result_paths = []

# CONVERT

length = len(audio_paths)
for i in range(length):
    print(f'Resolving format for {i+1} of {length}...')
    audio = audio_paths[i]

    title, extension = audio.split('.')
    if extension == "mp4":
        print(f'\tConverting {i+1} to mp3...')
        new_audio = tomp3.convert_mp4(audio, f'{title}.mp3')
        audio_paths[i] = new_audio

    if extension == "m4a":
        print(f'\tConverting {i+1} to mp3...')
        new_audio = tomp3.convert_m4a(audio, f'{title}.mp3')
        audio_paths[i] = new_audio

# SPLIT

SPLIT_PATH_BEGIN = "split"
division_chunks = []
for i in range(length):
    print(f'Resolving audio splitting for {i+1} of {length}...')
    audio = audio_paths[i]
    division_timestamps = divisions_timestamps[i]

    timestamps_length = len(division_timestamps)
    if timestamps_length > 0:
        print(f'\tSplitting into {timestamps_length+1} parts for {i+1}...')
        divided_chunk = split.divide(audio, f'{SPLIT_PATH_BEGIN}{i+1}', division_timestamps)
        division_chunks.append(divided_chunk)
        continue

    division_chunks.append([audio])

# TRANSCRIBE

for i in range(length):
    print(f'Transcribing {i+1} of {length}...')
    divided_chunk = division_chunks[i]

    transcription_parts = []
    parts_length = len(divided_chunk)
    for j in range(parts_length):
        if parts_length > 1:
            print(f'\tTranscribing division {j+1} of {parts_length}...')
        part = divided_chunk[j]

        transcribed_part = transc.transcribe(part)
        transcription_parts.append(transcribed_part)

    transcription = '\n'.join(transcription_parts)

    output_path = result_paths[i]
    with open(file=output_path, encoding='utf-8', mode='w') as w_file:
        w_file.write(transcription)

print("DONE")