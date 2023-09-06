import PyPDF2
import requests

response = requests.get(path)


path="https://www.ceec.edu.tw/files/file_pool/1/0n045359274947649605/02-112%E5%AD%B8%E6%B8%AC%E8%8B%B1%E6%96%87%E8%A9%A6%E5%8D%B7.pdf"
with open('sample.pdf', 'wb') as f:
    f.write(response.content)

pdfFileObj = open("sample.pdf", 'rb')
pdfReader = PyPDF2.PdfReader(pdfFileObj)

pageObj = pdfReader.pages[0]
pageObj.extract_text()

num=len(pdfReader.pages)
text=""
for x in range(1,num):
    pageObj = pdfReader.pages[x]
    text+=pageObj.extract_text()

part1=text.find("一、詞彙")
part2=text.find("二、綜合測驗")
part3=text.find("三、文意選填")
part4=text.find("四、篇章結構")
part5=text.find("五、閱讀測驗")
part6=text.find("第貳部分 、混合題")