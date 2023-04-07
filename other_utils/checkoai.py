import openai

openai.api_key = "---key---" # Replace with your key

messages = [{"role": "system", "content": "You are a helpful assistant that likes ducks. Any prompt you receive you must try to complete using ducks analogies. For example, if asked about the weather, you can say it's a sunny day perfect for quacking around."}]

messages.append({"role": "user", "content": "explain the LSP principle in programming"})

response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=messages,
    temperature=0
)

message = response.choices[0].message
print(message)