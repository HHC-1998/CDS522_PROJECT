from fastapi import FastAPI, Query, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from Data import Data
from ScanTxt import ScanTxt
from ScanTmo import ScanTmo
from ScanRcc import ScanRcc

# 初始化
application = FastAPI()

# 跨域问题解决方法（固定搭配）
application.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)


# 聊天交互链接
@application.get("/aitalk")
def AITalk(question : str = Query(None)):
    print(question)
    return "Can not answer now!"


# TXT文件交互链接
@application.post("/filetxt")
async def TaskTxt(File : UploadFile = File(None)):
    # 将二进制文件输出
    file = await File.read()
    await File.close()
    return ScanTxt().txtProcessor(file)


# PDF文件TMO交互链接
@application.post("/filetmo")
async def TaskTxt(File : UploadFile = File(None)):
    # 将二进制文件输出
    file = await File.read()
    await File.close()
    return ScanTmo().tmoProcessor(file)


# PDF文件RCC交互链接
@application.post("/filercc")
async def TaskTxt(File : UploadFile = File(None)):
    # 将二进制文件输出
    file = await File.read()
    await File.close()
    return ScanRcc().rccProcessor(file)


if __name__ == "__main__":
    # API接口参数
    uvicorn.run(app = "main:application", host = "localhost", port = 8000, reload = True)