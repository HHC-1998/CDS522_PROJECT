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
        self.db = "cds522_project"

    # 用于添加数据的方法
    def addData(self, dateReceived, source, hashtag, type, nameOfCaller, contactNo,
                slopeNo, location, natureOfRequest, subjectMatter, tenDayRuleDueDate,
                ICCInterimReplyDueDate, ICCFinalReplyDueDate, worksCompletionDueDate,
                faxToContractorOn, faxPages, caseDetails):
        # 链接数据库
        with pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, charset=self.charset, db=self.db) as addProcess:
        # 获取数据库链接工具
            with addProcess.cursor() as  addTool:
                try :
                    # sql语句添加功能
                    sql = "INSERT INTO complaininfo VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                    # 动态添加信息
                    parameters = [dateReceived, source, hashtag, type, nameOfCaller, contactNo,
                            slopeNo, location, natureOfRequest, subjectMatter, tenDayRuleDueDate,
                            ICCInterimReplyDueDate, ICCFinalReplyDueDate, worksCompletionDueDate,
                            faxToContractorOn, faxPages, caseDetails]
                    # 执行sqlyujv
                    addTool.execute(sql, args=parameters)
                    # 提交事务
                    addProcess.commit()
                except BaseException:
                    print(BaseException)

    # 用于查询数据的方法
    def queryData(self, sqlStatement):
        # 链接数据库
        with pymysql.connect(host=self.host, port=self.port, user=self.user, passwd=self.password, charset=self.charset, db=self.db) as queryProcess:
        # 获取数据库链接工具
            with queryProcess.cursor() as queryTool:
                try :
                    # sql语句查询功能
                    sql = sqlStatement
                    # 查找
                    queryTool.execute(sql)
                    # 返回查找信息
                    result = queryTool.fetchall()
                    return result
                except Exception as e:
                    print(e)

