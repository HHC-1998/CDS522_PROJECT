# 导入Data类
from Data import Data 
import PyPDF2
import io

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
        print(textContent)

        # 需要查找的值
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = [""] * 17

        # 提取信息字符串的方法
        def processStr(oldStr, keyName, valueLength):
            # 通过传入的键名算出键名的长度
            keyLength = len(keyName.split())
            # 通过空格分割字符串
            strList = oldStr.split()
            # 从中取出值
            valueList = strList[keyLength : keyLength + valueLength]
            # 将列表拼接回字符串
            newStr = " ".join(valueList)
            return newStr
                
        # 便利文件的每一行
        for str in textContent.split('\n'):
            a = processStr(str, "Date of Referral ", 3) if "Date of Referral " in str else "Null" 
            
        # 定义特定的值
        d, h, i, j, q= ["Null"] * 5
        b = "TMO"
        o = a
        
       
        return "null"



        

