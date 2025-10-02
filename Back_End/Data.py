# 数据类：所有类型的扫描类都可以调用此类来生成对象（后可连接数据库）
class Data:

    def __init__(self, dateRecieve, source, hashtag, nameOfCaller, contactNo, slopeNo,
                 TDRDD, ICCIRDD, ICCFRDD, faxToContractorOn, faxPages):
        self.dateRecieve = dateRecieve
        self.source = source
        self.hashtag = hashtag
        self.type = "Null"
        self.nameOfCaller = nameOfCaller
        self.contactNo = contactNo
        self.slopeNo = slopeNo
        self.location = "Null"
        self.natureOfRequest = "Null"
        self.subjectMatter = "Null"
        self.TDRDD = TDRDD
        self.ICCIRDD = ICCIRDD
        self.ICCFRDD = ICCFRDD
        self.worksCompletionDueDate = "Null"
        self.faxToContractorOn = faxToContractorOn
        self.faxPages = faxPages
        self.caseDetails = "Null"

    def __str__(self):
        return (f"a = {self.dateRecieve}\nb = {self.source}\nc = {self.hashtag}\n"
                f"d = {self.type}\ne = {self.nameOfCaller}\nf = {self.contactNo}\ng = {self.slopeNo}\n"
                f"h = {self.location}\ni = {self.natureOfRequest}\nj = {self.subjectMatter}\nk = {self.TDRDD}\n"
                f"l = {self.ICCIRDD}\nm = {self.ICCFRDD}\nn = {self.worksCompletionDueDate}\n"
                f"o = {self.faxToContractorOn}\np = {self.faxPages}\nq = {self.caseDetails}")
