import openai

INTERVIEW_PATH = "" # Replace with interview transcription
RESULT_PATH = "result.txt"

with open(file='prompt.txt', encoding='utf-8') as prompt_file:
    prompt = prompt_file.read()

with open(file=INTERVIEW_PATH, encoding='utf-8') as int_file:
    interview = int_file.read()

openai.api_key = "---key---" # Replace with your key
messages = [{"role": "system", "content": prompt}]

interview_parts = interview.split("###") # Interview file should be divided with '###' to not exceed the limit of 4000 tokens
result = ""
length = len(interview_parts)
last_reset_at = 0
for i in range(length):
    print(f'Processing message number {i + 1} of {length}...')
    part = interview_parts[i]

    messages.append({"role": "user", "content": part})

    if i - last_reset_at >= 2:
        print(f'Resetting for tokens on message number {i + 1}...')
        messages.clear()
        messages.append({"role": "system", "content": prompt})
        messages.append({"role": "user", "content": part})
        last_reset_at = i

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            temperature=0
        )
    except openai.InvalidRequestError as error:
        if "maximum context length" in str(error):
            print(f'Too many tokens, resetting on message number {i + 1}...')
            messages.clear()
            messages.append({"role": "system", "content": prompt})
            messages.append({"role": "user", "content": part})
            last_reset_at = i
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                temperature=0
            )

    message = response.choices[0].message
    messages.append(message)

    result += f'{message.content}\n###\n'

    print(f'Finished message number {i + 1} of {length}...')

with open(file=RESULT_PATH, encoding='utf-8', mode='w') as r_file:
    r_file.write(result)

print("DONE")