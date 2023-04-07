
def line(text: str):
    SEGMENT_SIZE = 100

    lined_text = ""
    words = text.split(' ')
    length = len(words)
    last_line_ended_at = 0
    for i in range(1, length):
        words_for_line = words[last_line_ended_at:i]
        line = ' '.join(words_for_line)
        if len(line) > SEGMENT_SIZE:
            lined_text += f'{line}\n'
            last_line_ended_at = i

    last_line_words = words[last_line_ended_at:length]
    last_line = ' '.join(last_line_words)
    lined_text += f'{last_line}\n'

    return lined_text


# with open(file='transcript.txt', encoding='utf-8') as r_file:
#     text = r_file.read()

# lined_text = line(text)

# with open(file="transcript_lined2.txt", encoding='utf-8', mode='w') as w_file:
#     w_file.write(lined_text)