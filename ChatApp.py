import toml
import openai

class ChatApp:
    with open("secrets.toml", "r") as f:
        config = toml.load(f)
    openai.api_key = config["OPENAI_KEY"]

    def __init__(self):
        self.messages = [{"role": "system", "content": "An intelligent Assistant"}]

    def chat(self, conversation):
        #self.messages.append({"role": "assistant", "content": conversation})
        #self.messages.append({"role": "user", "content": message})
        #print(str(self.messages))
        response = openai.ChatCompletion.create(
        model ="gpt-3.5-turbo",
        #model="gpt-4",
        temperature=1,
        messages =conversation
        )
        usage_tokens = response['usage']['total_tokens']
        #self.messages.append({"role": "assistant", "content": response["choices"][0]["message"].content})
        return response["choices"][0]["message"].content

