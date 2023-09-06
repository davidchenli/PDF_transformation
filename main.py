import PyPDF2
import requests
from src import first_part, second_part,third_part,forth_part,fifth_part,sixth_part,seventh_part
from datetime import datetime

path="https://www.ceec.edu.tw/files/file_pool/1/0n045359274947649605/02-112%E5%AD%B8%E6%B8%AC%E8%8B%B1%E6%96%87%E8%A9%A6%E5%8D%B7.pdf"



def test_transformation(path):
    response = requests.get(path)
    with open('input/sample.pdf', 'wb') as f:
        f.write(response.content)

    pdfFileObj = open("input/sample.pdf", 'rb')
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
    part7=text.find("第參部分、非選擇題")


    first=text[part1:part2]
    second=text[part2:part3]
    third=text[part3:part4]
    forth=text[part4:part5]
    fifth=text[part5:part6]
    sixth=text[part6:part7]
    senventh=text[part7:]

    partA=first_part(first)
    partB=second_part(second)
    partC=third_part(third)
    partD=forth_part(forth)
    partE=fifth_part(fifth)
    partF=sixth_part(sixth)
    partG=seventh_part(senventh)

    output={"url":path,
            "datetime":datetime.now(),
            "question":{
            "part1":partA,
            "part2":partB,
            "part3":partC,
            "part4":partD,
            "part5":partE,
            "part6":partF,
            "part7":partG}}

    return(output)




