# 导入Data类
from Data import Data 
import PyPDF2
import io

# 创建一个扫描TXT文件的类
class ScanTmo:

    # 构造函数
    def __init__(self):
        print("构造")

    # TXT文件扫描 
    def tmoProcessor(self, pdfContent):

        # 使用PyPdf2来操作pdf文件
        # io.BytesIO - 接收一个 “类文件对象” 参数，支持常见的文件操作方法如 read，write，seek
        # seek函数用于操作文件指针
        pdfReader = PyPDF2.PdfReader(io.BytesIO(pdfContent))
        
        # 只取出pdf的第一页即可
        # pages参数是一个包含PDF文档所有页面对象的列表式属性
        firstPage = pdfReader.pages[0]
