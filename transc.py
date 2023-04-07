import openai
import vtt_clean

def transcribe(file_path) -> str:
    with open(file='prompt.txt', encoding='utf-8') as prompt_file:
        prompt = prompt_file.read()

    audio = open(file_path, "rb")

    openai.api_key = "---key---" # Replace with your key
    transcript = openai.Audio.transcribe("whisper-1", audio, language="ro", prompt=prompt, temperature=0, response_format="vtt")
    # transcript = openai.Audio.transcribe("whisper-1", audio, language="ro", temperature=0, response_format="vtt")

    title, _ = file_path.split('.')
    with open(file=f'transc_logs/{title}_transc.txt', encoding='utf-8', mode='w') as w_file:
        w_file.write(transcript)

    return vtt_clean.clean(transcript)