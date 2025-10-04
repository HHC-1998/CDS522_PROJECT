# 这是一个数据库类，目前值适用于增加和检索数据
# 调用pymysql包来连接mysql数据库
import pymysql

class DataBase:
    
    def __init__(self):
        self.host = "localhost"
        self.port = 3306
        self.user = "root"
        self.password = "root"
        self.charset = "utf8"

    # 用于添加数据的方法
    def addData(self, dateReceived, source, hashtag, type, nameOfCaller, contactNo,
                 slopeNo, location, natureOfRequest, subjectMatter, tenDayRuleDueDate,
                 ICCInterimReplyDueDate, ICCFinalReplyDueDate, worksCompletionDueDate,
                 faxToContractorOn, faxPages, caseDetails):
        # 链接数据库
        addProcess = pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, charset=self.charset)
        # 获取数据库链接工具
        addTool = addProcess.cursor()
        # sql语句添加功能
        sql = ""
        # 执行sqlyujv
        addTool.execute(sql)
        # 关闭链接
        addTool.close