# 导入Data类
from Data import Data 
from pdf2image import convert_from_bytes # 用于操作PDF文件与图像之间的转换(基于Poppler工具集，需要一同配置)
import pytesseract # 用于操作图像与文本之间的操作

# 创建一个扫描TXT文件的类
class ScanRcc:

    # 构造函数
    def __init__(self):
        pass

    # TXT文件扫描 
    def rccProcessor(self, pdfContent):

        # convert_from_bytes - 直接将二进制PDF文件转化成图片列表
        # 可以选择起始页和中止页
        firstPageImg = convert_from_bytes(pdfContent, first_page=1, last_page=1)[0]

        # 将图片识别为文本信息
        # 使用pytesseract前要确定poppler，tesseract，tessdata的Path都已配置妥当
        textContent = pytesseract.image_to_string(firstPageImg, lang = "chi_sim+chi_tra+eng")
