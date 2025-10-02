# 导入Data类
from Data import Data 

# 创建一个扫描TXT文件的类
class ScanTmo:

    # 构造函数
    def __init__(self, file):
        self.file = file

    # TXT文件扫描 
    def tmoProcessor(self):
        print()