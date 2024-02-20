from tkinter import filedialog
from tkinter import messagebox

def cleaning(code):
    code=[s.split("//")[0] for s in code]
    code=[s.replace("\n",'') for s in code]
    code=[s.strip() for s in code]
    code=[x for x in code if x!='']

    return code

def arithmetic(code,i):
    dictionary= {'add':["@SP","AM=M-1","D=M","A=A-1","M=D+M"],
        'sub':["@SP","AM=M-1","D=M","A=A-1","M=M-D"],
        "neg":["@SP","A=M-1","M=M-1","M=-M"],
        "not":["@SP","A=M-1","M=!M"],
        "and":["@SP","AM=M-1","D=M","A=A-1","M=D&M"],
        "or":["@SP","AM=M-1","D=M","A=A-1","M=D|M"],
        "eq":["@SP","M=M-1","A=M","D=M","A=A-1","D=M-D","@YES"+str(i),"D;JEQ","@SP","A=M-1","M=0","@END"+str(i)," 0;JMP","(YES"+str(i)+")","@SP","A=M-1","M=-1","(END"+str(i)+")"],
        "gt":["@SP","M=M-1","A=M","D=M","A=A-1","D=M-D","@YES"+str(i),"D;JGT","@SP","A=M-1","M=0","@END"+str(i)," 0;JMP","(YES"+str(i)+")","@SP","A=M-1","M=-1","(END"+str(i)+")"],
        "lt":["@SP","M=M-1","A=M","D=M","A=A-1","D=M-D","@YES"+str(i),"D;JLT","@SP","A=M-1","M=0","@END"+str(i)," 0;JMP","(YES"+str(i)+")","@SP","A=M-1","M=-1","(END"+str(i)+")"]}


    return dictionary[code]


def push(code,filename):
    v = code.split(" ")
    if v[1]=='constant':
        i = v[2]
        l = ["@"+i,"D=A","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=='local':
        i=v[2]
        l = ["@"+i,"D=A","@LCL","A=D+M","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=='argument':
        i=v[2]
        l = ["@"+i,"D=A","@ARG","A=D+M","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=='temp':      
        i=v[2]
        l = ["@"+i,"D=A","@5","A=A+D","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=='this':
        i=v[2]
        l = ["@"+i,"D=A","@THIS","A=D+M","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=='that':
        i=v[2]
        l = ["@"+i,"D=A","@THAT","A=D+M","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=="pointer":
        if v[2]=='0':
            l=["@THIS","D=M","@SP","A=M","M=D","@SP","M=M+1"]
        else:
            l=["@THAT","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    elif v[1]=="static":
        i=v[2]
        l=["@"+filename+"."+v[2],"D=M","@SP","A=M","M=D","@SP","M=M+1"]


    return l


def pop(code,filename):
    v = code.split(" ")
    if v[1]=='local':
        i=v[2]
        l = ["@"+i,"D=A","@LCL","D=D+M","@13","M=D","@SP","AM=M-1","D=M","@13","A=M","M=D"]
    elif v[1]=='argument':
        i=v[2]
        l = ["@"+i,"D=A","@ARG","D=D+M","@13","M=D","@SP","AM=M-1","D=M","@13","A=M","M=D"]
    elif v[1]=='temp':
        i=v[2]
        l = ["@"+i,"D=A","@5","D=D+A","@13","M=D","@SP","AM=M-1","D=M","@13","A=M","M=D"]
    elif v[1]=='this':
        i=v[2]
        l = ["@"+i,"D=A","@THIS","D=D+M","@13","M=D","@SP","AM=M-1","D=M","@13","A=M","M=D"]
    elif v[1]=='that':
        i=v[2]
        l = ["@"+i,"D=A","@THAT","D=D+M","@13","M=D","@SP","AM=M-1","D=M","@13","A=M","M=D"]
    elif v[1]=="pointer":
        if v[2]=='0':
            l=["@SP","AM=M-1","D=M","@THIS","M=D"]
        else:
            l=["@SP","AM=M-1","D=M","@THAT","M=D"]
    elif v[1]=="static":
        i=v[2]
        l = ["@SP","AM=M-1","D=M","@"+filename+"."+v[2],"M=D"]

    return l

def label(code):
    k = code.split(" ")
    l = ["("+k[1]+")"]
    
    return l;

def goto(code):
    k= code.split(" ")
    l = ["@"+k[1],"0;JMP"]

    return l


def ifgoto(code):
    k = code.split(" ")
    l = ["@SP","AM=M-1","D=M","@"+k[1],"D;JNE"]
    return l


def function(code):
    k = code.split(" ")
    l = ["("+k[1]+")"]
    for i in range(int(k[2])):
        l = l+["@SP", "A=M", "M=0", "@SP", "M=M+1"]
    
    return l

def call(code,callcount):
    k = code.split(" ")
    label = k[1] + "call" + str(callcount)
    l = ["@"+label,"D=A","@SP","A=M","M=D","@SP","M=M+1"]
    l = l + ["@LCL","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    l = l + ["@ARG","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    l = l + ["@THIS","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    l = l + ["@THAT","D=M","@SP","A=M","M=D","@SP","M=M+1"]
    l = l + ["@SP","D=M","@LCL","M=D","@5","D=D-A","@"+k[2],"D=D-A","@ARG","M=D"]
    l = l + ["@"+k[1],"0;JMP"]
    l = l + ["("+label+")"]
    return l

def returncall():
    l =   ["@LCL","D=M","@13","M=D",
        "@5","A=D-A","D=M","@14","M=D",
        "@SP","AM=M-1","D=M","@ARG","A=M","M=D","@ARG","D=M","@SP","M=D+1",
        "@13","AM=M-1","D=M","@THAT","M=D",
        "@13","AM=M-1","D=M","@THIS","M=D",
        "@13","AM=M-1","D=M","@ARG","M=D",
        "@13","AM=M-1","D=M","@LCL","M=D",
        "@14","A=M","0;JMP"]

    return l


name=filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("Text files",".txt"),("vm files",".vm")))
file = open(name,'r')
code = file.readlines()
file.close()

no_of_files = 1
filename = name.split('/')[-1].split(".")[0]
writename = name.split("/")[-2]
fileslist = [filename]
directory = name.replace(filename+".vm","")
acount=0;
callcount = 1;

code = cleaning(code)
for x in code:
    k = x.split(" ")
    if k[0]=='call':
        if k[1].split(".")[0] in fileslist:
            pass
        else:
            file = open(directory+k[1].split(".")[0]+".vm",'r')
            code  = code + file.readlines()
            file.close()
            fileslist.append(k[1].split(".")[0])
            no_of_files = no_of_files + 1


print(fileslist)
code = cleaning(code)


if(no_of_files==1):
    list2=["@256","D=A","@SP","M=D"]
    list2 = list2+call("call Main.main 0", 0)

else:
    list2=["@256","D=A","@SP","M=D"]
    list2 = list2+call("call Sys.init 0", 0)
    filename = "Sys"


for x in code:
    k=x.split(" ")
    if (len(k)==1):
        if(x=="return"):
            v= returncall()
            list2 = list2 + v
        else:
            acount = acount + 1;
            v = arithmetic(x, acount)
            list2= list2 + v
    else:
        if(k[0]=='push'):
            v = push(x,filename)
            list2= list2 + v
        elif(k[0]=="pop"):
            v=pop(x,filename)
            list2=list2 + v
        elif(k[0]=="label"):
            v=label(x)
            list2 = list2 + v
        elif(k[0]=="goto"):
            v=goto(x)
            list2 = list2 + v
        elif(k[0]=="if-goto"):
            v=ifgoto(x)
            list2 = list2 + v
        elif(k[0]=="function"):
            if len(k[1].split(".")) != 1:
                filename = k[1].split(".")[0]
            v = function(x)
            list2 = list2 +v
        elif(k[0]=="call"):
            v = call(x,callcount)
            callcount = callcount + 1
            list2 = list2 + v


list2 = list2 +["(THANOSWASRIGHT)","@THANOSWASRIGHT","0;JMP"]
list2 = [s+"\n" for s in list2]
print(list2)
name2 = directory+"/"+writename+".asm"
file2 = open(name2,'w')
file2.writelines(list2)
messagebox.showinfo("showinfo", "The Assembly language file is written in"+name2)