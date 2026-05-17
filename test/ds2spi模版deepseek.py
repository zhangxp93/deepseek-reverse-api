from openai import OpenAI

# 初始化客户端
# base_url 必须指向你本地运行的 ds2api 地址
# 注意：路径通常需要包含 /v1
client = OpenAI(
    api_key="RGUeKEJJZSOJtW80auncWmlh/ClyALPmNlizDOOv0RpJctwutrhZlSYRctAtZHFg",
    base_url="http://localhost:8000/v1"
    # base_url="http://172.16.45.5:5001/v1"
)

def chat_with_deepseek(prompt):
    try:
        response = client.chat.completions.create(
            # 模型名称：对应 config.json 中的 model_aliases 或原名
            # model="deepseek-v4-pro-search",
            model="deepseek-v4-flash",
            messages=[
                {"role": "system", "content": "你是一个专业的测试工程专家。"},
                {"role": "user", "content": prompt}
            ],
            stream=True  # 开启流式传输，体验更好
        )

        print("AI 响应：", end="")
        for chunk in response:
            if chunk.choices[0].delta.content:
                print(chunk.choices[0].delta.content, end="", flush=True)
        print("\n")

    except Exception as e:
        print(f"调用失败: {e}")

if __name__ == "__main__":
    user_input = "你的大模型版本，你可以做些什么，现在的时间"
    chat_with_deepseek(user_input)