import openai

# Setting API key
# You can obtain your key via
# https://platform.openai.com/account/api-keys
openai.api_key = ""

# ChatGPT Context
context = {"role": "system",
           "content": "Hello World!"}

# Colors
GREEN = "\033[92m"
RESET = "\033[0m"

while True:

    messages = [context]
    print(GREEN + ">> How can I help you?" + RESET + "(exit)")
    content = input(": ")

    # Ending the loop
    if content == "exit":
        exit("Bye")

    # Append
    messages.append({"role": "user", "content": content})

    # Setting up the response
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)
    response_content = response.choices[0].message.content

    # Append
    messages.append({"role": "assistant", "content": response_content})

    # Printing response
    print(f"{GREEN}>> {response_content} \n")
