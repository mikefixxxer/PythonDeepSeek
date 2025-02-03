from openai import OpenAI

# Point to the local server
client = OpenAI(base_url="http://localhost:1234/v1",
                api_key="lm-studio")

completion = client.chat.completions.create(
  model="deepseek-coder-33b-instruct-pythagora-v3",
  #model="deepseek-R1-Distill-Llama-8B",
  messages=[
    {"role": "system", "content": "Always answer in rhymes."},
    {"role": "user", "content": "Introduce yourself."}
  ],
  temperature=0.7,
)

print(completion.choices[0].message)