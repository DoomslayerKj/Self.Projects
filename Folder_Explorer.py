import os
from datetime import datetime
os.chdir("C:/Users/Varad Kj/PycharmProjects/OS_Modules")

def createAnewFile(name):
    f= open(name+".txt","w")
    f.close

def CreateNewFolder(name):
    os.makedirs(name)

def RenameFiles(name,to_name):
    os.rename(name,to_name)

def fileInfo(name):
    print(os.stat())
    
 
f =open("test_file.txt","w+",encoding="utf-8")
string =""
for dirpath,dirnames,filenames in os.walk(str(os.curdir)):
    print('Current Path : ',dirpath)
    print("dirnames",dirnames)
    print("filenames",filenames)

    string ="Current Path :"+str(dirpath)+"\ndirnames"+str(dirnames)+"\nfilenames"+str(filenames)
    f.writelines(str(string))
    f.write("\n\n\n")

f.close()


