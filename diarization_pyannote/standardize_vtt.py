
def vtt_time_to_millis(time):
    hours, minutes, seconds_and_millis = time.split(':')
    hours_millis = int(hours) * 60 * 60 * 1000
    minutes_millis = int(minutes) * 60 * 1000
    seconds, millis = seconds_and_millis.split('.')
    seconds_millis = int(seconds) * 1000
    return hours_millis + minutes_millis + seconds_millis + int(millis)

def standardize(vtt_path):
    TIMES_DIVIDER = "-->"

    with open(vtt_path, encoding='utf-8', mode='r') as r_file:
        diariz = r_file.read().splitlines()

    text = ""
    for line in diariz:
        is_vtt_mark = "WEBVTT" in line
        is_empty = not line
        if is_vtt_mark or is_empty:
            continue

        is_speech = TIMES_DIVIDER not in line
        if is_speech:
            text += f'{line}\n'
            continue    

        start, end = line.strip().split(TIMES_DIVIDER)
        start_millis = vtt_time_to_millis(start)
        end_millis = vtt_time_to_millis(end)
        text += f'{start_millis}:{end_millis}\n'

    return text