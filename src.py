import re

def first_part(test)
    regex = r"\n[0-9]+.[A-Za-z\n\,\.\_\'\"\’\“\”\?\!  ]+"
    match = re.findall(regex, test)   
    question=[x.strip().replace("\n"," ").replace("        "," _ ").replace("  "," ") for x in match]
    regex = r"\(A\)[A-Za-z\(\) ]+\n"
    match = re.findall(regex, test) 

    part1=[]
    for x in range(len(match)):
        
        
        tmp=match[x].split(" ")
        tmp=[x for x in tmp if x !="" and x!="\n"]
        Q=question[x]
        number=int(Q[:2].replace(".",""))
        options={
        tmp[0].replace("(","").replace(")",""):tmp[1],
        tmp[2].replace("(","").replace(")",""):tmp[3],
        tmp[4].replace("(","").replace(")",""):tmp[5],
        tmp[6].replace("(","").replace(")",""):tmp[7]
        }
        
        part1.append({"id":number,
        "question":Q[2:].strip(),
        "options":options
        })

    return part1
    
def second_part(test):

    test=test.split("題組")
    part2=[]
    for x in range(1,len(test)):
        tmp=test[x].split("\n \n")
        question=tmp[0].strip()
        
        
        regex = r"[0-9]+\."
        ids = re.findall(regex, tmp[1]) 
        regex = r"\([A-Z]\)[A-Za-z\(\) ]+"
        option = re.findall(regex, tmp[1]) 
        part=[]
        for x in range(len(ids)):
            number=ids[x]
            tmp=option[x].split(" ")
            tmp=[x for x in tmp if x !="" and x!="\n"]
            lens=(len(tmp)-4)/4
            options={
                tmp[0].replace("(","").replace(")",""):" ".join(tmp[1:1+int(lens)]),
                tmp[1+int(lens)].replace("(","").replace(")",""):" ".join(tmp[2+int(lens):2+2*int(lens)]),
                tmp[2+2*int(lens)].replace("(","").replace(")",""):" ".join(tmp[3+2*int(lens):3+3*int(lens)]),
                tmp[3+3*int(lens)].replace("(","").replace(")",""):" ".join(tmp[4+3*int(lens):4+4*int(lens)])
                }
            part.append({"id":number,
                "options":options
                })
        part2.append({"id":ids,
        "article":question,
        "options":part
            })
    return part2


def third_part(test):
    part3=[]
    test=test.split("題組")
    for x in range(1,len(test)):
        
        regex = r"[0-9][0-9]"
        number = re.findall(regex, test[x]) 
        number=[x for x in number if int(x)>20 and int(x)<30]
        question=test[x].split("\n \n")[0].strip()
        option=test[x].split("\n \n")[1]
        option=option.split("  ")
        ans={}
        for x in option:
            if x :
                a=x.strip().split(" ")
                ans.update({a[0].replace("(","").replace(")",""):" ".join(a[1:])})
        part3.append({"id":number,"article":question,"option":ans})
    return part3


def forth_part(test):
    part4=[]
    test=test.split("題組")
    regex = r"[0-9][0-9]"
    
    for x in range(1,len(test)):
        
        number = re.findall(regex, test[x]) 
        number=[x for x in number if int(x)>30 and int(x)<40]
        question=test[x].split("\n \n")[0].strip()
        options=test[x].split("\n \n")[1].split("\n")
        ans={}
        for x in options:
            if x :
                a=x.strip().split(" ")
                ans.update({a[0].replace("(","").replace(")",""):" ".join(a[1:])})
        part4.append({"id":number,"article":question,"option":ans})
    return part4


def fifth_part(test):
    part5=[]
    test=test.split("題組")
    for x in range(1,len(test)):
    
        regex = r"\n[0-9]+. [A-Za-z\n\,\.\_\'\"\’\“\”\?\!  ]+"
        match = re.findall(regex, test[x])

        number=[x.strip()[:2] for x in match]    

        questuon=[x.strip()[4:] for x in match]  

        regex = r"\(A\) [A-Za-z\n\,\.\_\'\"\’\“\”\?\! \-]+"
        match = re.findall(regex, test[x]) 
        As=[x.strip()[4:] for x in match]

        regex = r"\(B\)[A-Za-z\n\,\.\_\'\"\’\“\”\?\! \-]+"
        match = re.findall(regex, test[x]) 
        Bs=[x.strip()[4:] for x in match]

        regex = r"\(C\)[A-Za-z\n\,\.\_\'\"\’\“\”\?\! \-]+"
        match = re.findall(regex, test[x]) 
        Cs=[x.strip()[4:] for x in match]

        regex = r"\(D\)[A-Za-z\n\,\.\_\'\"\’\“\”\?\! \-]+"
        match = re.findall(regex, test[x]) 
        Ds=[x.strip()[4:] for x in match]

        options=[]
        for x in range(len(number)):
            options.append([{"id":number[x],
            "question":questuon[x],
            "options":{"A":As[x],"B":Bs[x],"C":Cs[x],"D":Ds[x]}}])
            
        article=test[x][:test[x].find("\n"+number[0])].strip()
        part5.append({
        "id":number,
        "article":article,
        "options":options})
        
    return part5