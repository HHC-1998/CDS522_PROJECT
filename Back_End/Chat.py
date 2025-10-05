import os
from openai import OpenAI

# 实现AI对话及数据库调用
class Chat:

    def __init__(self):
        self.key = "sk-36fe9d5a8af8453c9b0fcc2c8f0b93c2"
        self.url = "https://api.deepseek.com"

    # ai聊天功能的实现方法
    def aiTalk(self, question):

        # 调用DeepSeek官网提供的api接口
        # 输入DeepSeek提供的密钥和端口
        client = OpenAI(api_key=self.key, base_url=self.url)

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "你是专业客服，负责解答用户疑问。用友好语气回应，高效解决问题。"},
                {"role": "user", "content": question},
            ],
            stream=False
        )

        return response.choices[0].message.content