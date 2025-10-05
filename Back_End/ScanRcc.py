# 导入Data类
from Data import Data 
from pdf2image import convert_from_bytes # 用于操作PDF文件与图像之间的转换(基于Poppler工具集，需要一同配置)
import pytesseract # 用于操作图像与文本之间的操作
from datetime import datetime, timedelta

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
        # 在控制台显示文本文件
        print(textContent)
            
        # 处理查找到的字符串
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


        # 需要查找的值
        a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q = ["Null"] * 17

        # 遍历文本文件
        for str in textContent.split('\n'):
            if "Handle Date:" in str : a = processStr(str, "Handle Date:", 1)
            if "Call Reference No.:" in str : c = processStr(str, "Call Reference No.:", 1)
            if "Name of Client:" in str : e = processStr(str, "Name of Client:", 1)
            if "Contact Tel No:" in str : f = processStr(str, "Contact Tel No:", 1)
            if "Slope No." in str : g = processStr(str, "Slope No.", 1)
            

        # 算出十天之后的日期
        def tenDayLate(nowDate):
            # 先将字符串转化为日期 ： strptime是字符转日期， strftime是日期转字符
            date = datetime.strptime(nowDate, "%Y/%m/%d")
            # 通过日期类型算出10天以后的日期 : timedelta用于算时间间隔和时间差
            tenDay = date + timedelta(days=10)
            # 再将日期转化为字符串
            tenDayStr = datetime.strftime(tenDay, "%Y/%m/%d")
            return tenDayStr


         # 定义特定的值
        d, h, i, j, q= ["Null"] * 5
        b = "RCC"
        if a != "Null" : k = tenDayLate(a)
        o = a

        # 返回一个数据对象 
        extractInfo = Data(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
        return extractInfo
