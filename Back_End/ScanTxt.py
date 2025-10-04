# 导入Data类
from Data import Data

# 创建一个扫描TXT文件的类
class ScanTxt:

    # 构造函数
    def __init__(self):
        pass

    # TXT文件扫描 
    def txtProcessor(self, txtContent):

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
        for i in txtContent.split('\n'):
            if i.startswith("Case Creation Date") : a = processStr(i)                 # a
            if i.startswith("1823 CASE") : c = processStr(i)                          # c
            if i.startswith("Last Name") : e = processStr(i)                          # e
            if i.startswith("Mobile") : f1 = processStr(i)                            # f1
            if i.startswith("Email Address") : f2 = processStr(i)                     # f2
            if i.startswith("Re-assignment") : k = processStr(i)                      # k
            if i.startswith("Interim Reply") : l = processStr(i)                      # l
            if i.startswith("Final Reply") : m = processStr(i)                        # m

        # 定义特定的值
        f = f1 + "/" + f2
        d, h, i, j, q = "Null"
        b = "ICC"
        o = a
        p = "Connot Found"

        # 返回一个数据对象 
        extractInfo = Data(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q)
        return extractInfo

