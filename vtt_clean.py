
def clean(text) -> str:
    lines = text.splitlines()
    output = ""
    for line in lines:
        is_vtt_mark = "WEBVTT" in line
        is_empty = not line
        is_timestamp = "-->" in line
        if is_vtt_mark or is_empty or is_timestamp:
            continue
        output += f'{line}\n'
    return output