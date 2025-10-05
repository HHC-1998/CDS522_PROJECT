# 导入Data类
from Data import Data
import chardet

# 创建一个扫描TXT文件的类
class ScanTxt:

    # 构造函数
    def __init__(self):
        pass

    # TXT文件扫描 
    def txtProcessor(self, txtContent):

        # 根据文件不同的编码方式进行解码
        fileDetail = chardet.detect(txtContent)
        txtContent = txtContent.decode(fileDetail["encoding"])

        # 处理查找到的字符串
        def processStr(oldStr):
            newStr = oldStr.split(":")[1].strip()
            if(len(newStr) != 0):
                return newStr
            else:
                return "Null"

        # 需要查找的值
        a, b, c, d, e, f1, f2, g, h, i, j, k, l, m, n, o, p, q = [""] * 18

        # 逐行遍历该字符串
        for str in txtContent.split('\n'):
            if "Case Creation Date" in str : a = processStr(str).split()[0]      # a
            if "1823 CASE" in str : c = processStr(str)                          # c
            if "Last Name" in str : e = processStr(str)                          # e
            if "Mobile" in str : f1 = processStr(str)                            # f1
            if "Email Address" in str : f2 = processStr(str)                     # f2
            if "斜坡編號為" in str : g = str                                      # g
            if "Re-assignment" in str : k = processStr(str).split()[0]           # k
            if "Interim Reply" in str : l = processStr(str).split()[0]           # l
            if "Final Reply" in str : m = processStr(str).split()[0]             # m

        # 定义特定的值
        f = f1 + "/" + f2
        d, h, i, j, q, n = ["Null"] * 6
        b = "ICC"
        o = a
        p = "Connot Found"

        # 返回一个数据对象 
        extractInfo = Data(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
        return extractInfo

