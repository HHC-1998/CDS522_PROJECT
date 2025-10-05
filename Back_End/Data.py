from DataBase import DataBase

# 数据类：所有类型的扫描类都可以调用此类来生成对象（后可连接数据库）
class Data:

    def __init__(self, dateReceived, source, hashtag, type, nameOfCaller, contactNo,
                 slopeNo, location, natureOfRequest, subjectMatter, tenDayRuleDueDate,
                 ICCInterimReplyDueDate, ICCFinalReplyDueDate, worksCompletionDueDate,
                 faxToContractorOn, faxPages, caseDetails):
        
        self.dateReceived = dateReceived
        self.source = source
        self.hashtag = hashtag
        self.type = type
        self.nameOfCaller = nameOfCaller
        self.contactNo = contactNo
        self.slopeNo = slopeNo
        self.location = location
        self.natureOfRequest = natureOfRequest
        self.subjectMatter = subjectMatter
        self.tenDayRuleDueDate = tenDayRuleDueDate
        self.ICCInterimReplyDueDate = ICCInterimReplyDueDate
        self.ICCFinalReplyDueDate = ICCFinalReplyDueDate
        self.worksCompletionDueDate = worksCompletionDueDate
        self.faxToContractorOn = faxToContractorOn
        self.faxPages = faxPages
        self.caseDetails = caseDetails
        # 创建对象的同时将对象信息写入数据库
        DataBase().addData(dateReceived, source, hashtag, type, nameOfCaller, contactNo, slopeNo, location, natureOfRequest, 
                          subjectMatter, tenDayRuleDueDate, ICCInterimReplyDueDate, ICCFinalReplyDueDate, worksCompletionDueDate,
                          faxToContractorOn, faxPages, caseDetails)

    # 重写toString方法
    def __str__(self):
        return (f"a = {self.dateReceived}\nb = {self.source}\nc = {self.hashtag}\nd = {self.type}\n"
                f"e = {self.nameOfCaller}\nf = {self.contactNo}\ng = {self.slopeNo}\n"
                f"h = {self.location}\ni = {self.natureOfRequest}\nj = {self.subjectMatter}\nk = {self.tenDayRuleDueDate}\n"
                f"l = {self.ICCInterimReplyDueDate}\nm = {self.ICCFinalReplyDueDate}\nn = {self.worksCompletionDueDate}\n"
                f"o = {self.faxToContractorOn}\np = {self.faxPages}\nq = {self.caseDetails}")
