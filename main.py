import openai

API_KEY = '你的API密钥'

openai.api_key = API_KEY

def get_resp():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "给我一个 Python 请求 OpenAI Chat 的 demo."}
        ],
        max_tokens=150,
        temperature=0.7,
    )
    return response['choices'][0]['message']['content']

if __name__ == '__main__':
    print(get_resp())
