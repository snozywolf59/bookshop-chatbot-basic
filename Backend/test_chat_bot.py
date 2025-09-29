import ollama

from utils  import prepare_prompt

prompt = prepare_prompt("Harry Potter và Hòn Đá Phù Thủy")
response = ollama.chat(
    model="gemma3:1b",
    messages=[{"role": "user", "content": prompt}]
)

print(response["message"]["content"])