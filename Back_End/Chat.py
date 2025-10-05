import os
from openai import OpenAI
from DataBase import DataBase

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

        # 第一次连接主要是为了生成查询使用的sql语句
        # 第一个人工智能的身份
        firstAI = "你现在是一名专业的数据库查询与业务分析助手，负责处理基于以下数据库表的各类需求。请严格基于表结构信息回应，确保所有操作都围绕表中列展开表中包含以下列（所有列的数据类型均为 varchar(100): - dateReceived: 案件接收日期- source: 案件来源（如RCC, TMO, 1823等）- hashtag: 案件编号- type: 案件类型（如投诉、咨询、申请等）- nameOfCaller: 诉求人姓- contactNo: 诉求人联系方式（电话/邮箱）- slopeNo: 边坡编号（关联具体工程场景）- location: 位置信息- natureOfRequest: 诉求性质（如维修、信息查询等）- subjectMatter: 诉求主题- tenDayRuleDueDate: 10天规则到期日- ICCInterimReplyDueDate: ICC临时回复到期日- ICCFinalReplyDueDate: ICC最终回复到期日- worksCompletionDueDate: 工程完成到期日- faxToContractorOn: 发给承包商的传真日期- faxPages: 传真页数- caseDetails: 案件详细描述当用户提出查询需求（如“统计不同来源的案件数量”“查询未按时回复的案件”），需基于上述列严格生成对应的SQL查询语句注意：因所有列均为varchar类型，日期类字段（如dateReceived、各类DueDate）需用字符串处理函数，例如MySQL中可用STR_TO_DATE()转换后比较，数据库名是cds522_project，表名是complaininfo，你只负责生成一个严格的mysql查询语句，其他的都不要说。"

        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": firstAI},
                {"role": "user", "content": question},
            ],
            stream=False
        )
        # 查看ai生成的Query语句
        print("Query SQL Statement : ", response.choices[0].message.content)
        
        # 查询
        dataResult = DataBase().queryData(response.choices[0].message.content)

        # 第二次连接主要是为了回答用户
        # 第二个人工智能的身份
        firstAI = "查询结果应答助手”，核心职责：接收数据库返回的元组格式查询结果并分析其中的数据，结合客户原始问题，用自然语言总结回答；若结果为空你也要告知用户，要把元组中的具体信息都告诉用户。"
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": firstAI},
                {"role": "user", "content": f"用户问题：{question} ， 数据库返回结果：{dataResult}"},
            ],
            stream=False
        )
        return response.choices[0].message.content