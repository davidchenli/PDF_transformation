import re

def first_part(test)
    regex = r"\n[0-9]+.[A-Za-z\n\,\.\_\'\"\’\“\”\?\!  ]+"
    match = re.findall(regex, test)   
    question=[x.strip().replace("\n"," ").replace("        "," _ ").replace("  "," ") for x in match]
    regex = r"\(A\)[A-Za-z\(\) ]+\n"
    match = re.findall(regex, test) 

    part1=[]
    for x in range(10):
        
        
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
    
