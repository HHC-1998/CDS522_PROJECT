# 导入Data类
from Data import Data 
import PyPDF2
import io
from datetime import datetime, timedelta

# 创建一个扫描PDF文件的类
class ScanTmo:

    # 构造函数
    def __init__(self):
        pass

    # PDF文件扫描 
    def tmoProcessor(self, pdfContent):

        # 使用PyPdf2来操作pdf文件
        # io.BytesIO - 接收一个 “类文件对象” 参数，支持常见的文件操作方法如 read，write，seek
        # seek函数用于操作文件指针
        pdfReader = PyPDF2.PdfReader(io.BytesIO(pdfContent))
        
        # 只取出pdf的第一页即可
        # pages参数是一个包含PDF文档所有页面对象的列表式属性
        firstPage = pdfReader.pages[0]

        # extract_text可以将pdf中的文本信息提取成字符串
        textContent = firstPage.extract_text()
        # 在控制台显示文本文件
        print(textContent)

        # 需要查找的值
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = ["Null"] * 17

        # 提取信息字符串的方法
        def processStr(oldStr, keyName, valueLength):
            # 通过空格分割字符串
            strList = oldStr.split()
            # 分割键名
            keyList = keyName.split()
            # 键名最后一个元素在原句中的索引
            keyIndex = strList.index(keyList[-1])
            # 从中取出值
            valueList = strList[keyIndex + 1 : keyIndex + valueLength + 1]
            # 将列表拼接回字符串
            newStr = " ".join(valueList)
            return newStr
            # # 通过传入的键名算出键名的长度
            # keyLength = len(keyName.split())
            # # 通过空格分割字符串
            # strList = oldStr.split()
            # # 从中取出值
            # valueList = strList[keyLength : keyLength + valueLength]
            # # 将列表拼接回字符串
            # newStr = " ".join(valueList)
            # if len(newStr) == 0 : newStr = "Null"
            # return newStr

        # 算出十天之后的日期
        def tenDayLate(nowDate):
            # 先将字符串转化为日期 ： strptime是字符转日期， strftime是日期转字符
            date = datetime.strptime(nowDate, "%d %B %Y")
            # 通过日期类型算出10天以后的日期 : timedelta用于算时间间隔和时间差
            tenDay = date + timedelta(days=10)
            # 再将日期转化为字符串
            tenDayStr = datetime.strftime(tenDay, "%d %B %Y")
            return tenDayStr


        # 便利文件的每一行
        for str in textContent.split('\n'):
            if "Date of Referral" in str : a = processStr(str, "Date of Referral", 3)
            if "Slope no." in str: g = processStr(str, "Slope no.", 2)  
     
        # 定义特定的值
        e, f = ["TMO(DEVB)"] * 2
        if a != "Null" : k = tenDayLate(a)
        b = "TMO"
        o = a
        p = "Connot Found"
        
        # 返回一个数据对象 
        extractInfo = Data(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
        return extractInfo



        

