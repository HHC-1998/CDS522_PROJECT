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
        a, c, e, f1, f2, g, k, l, m = [""] * 9
        # 逐行遍历该字符串
        for i in txtContent.split('\n'):
            if i.startswith("Case Creation Date") : a = processStr(i)                       # a
            if i.startswith("1823 CASE") : c = processStr(i)                                # c
            if i.startswith("Last Name") : e = processStr(i)                                # e
            if i.startswith("Mobile") : f1 = processStr(i)                                  # f1
            if i.startswith("Email Address") : f2 = processStr(i)                           # f2
            if i.startswith("投訴人") : g = i                                                # g
            if i.startswith("Re-assignment") : k = processStr(i)                            # k
            if i.startswith("Interim Reply") : l = processStr(i)                            # l
            if i.startswith("Final Reply") : m = processStr(i)                              # m
        # 特定值或未找到值
        b, o, p = "ICC", a, "Con not found"

        # 返回一个数据对象 
        extractInfo = Data(a, b, c, e, f1+"/"+f2, g, k, l, m, o, p)
        return extractInfo

