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

        # 需要查找的值
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = [""] * 17

        # # 逐行遍历该字符串
        # for i in textContent.split('\n'):
        #     if "Date of Referral" in i : a = i.find("Date of Referral")                   # a
        #     # if "Slope no." in i : g = processStr(i)                          # g
        #     # if "Re-assignment" in i : k = processStr(i)                      # k
        #     # if "Interim Reply" in i : l = processStr(i)                      # l
        #     # if "Final Reply" in i : m = processStr(i)                        # m

        # # 定义特定的值
        # d, h, i, j, q, n = ["Null"] * 6
        # b = "TMO"
        # c, e, f = ["TMO(DEVB)"] * 3
        # o = a
        # p = "Connot Found"

        # # 返回一个数据对象 
        # extractInfo = Data(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
        # return extractInfo
        return "TMO OK"



        

